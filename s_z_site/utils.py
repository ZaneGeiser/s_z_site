from django.utils.text import slugify
from django.core.files import File
from pathlib import Path
from PIL import Image
from io import BytesIO

#fallen out of use with upgrade to WagTail
def unique_slug_generator(instance):
    """ 
    :param model_instance:
    :param instance:
    :return:
    """
    slug = slugify(str(instance.title))
    model_class = instance.__class__

    while model_class._default_manager.filter(slug=slug).exists():
        latest_object = model_class._default_manager.latest('pk')
        new_object_pk = latest_object.pk + 1

        slug = f'{slug}-{new_object_pk}'

    return slug


#Image Resizing prior to AWS Upload
image_types = {
    "jpg": "JPEG",
    "jpeg": "JPEG",
    "png": "PNG",
    "gif": "GIF",
    "tif": "TIFF",
    "tiff": "TIFF",
}

def image_resize(image, width, height):
    # Open the image using Pillow
    img = Image.open(image)
    # check if either the width or height is greater than the max
    if img.width > width or img.height > height:
        output_size = (width, height)
        # Create a new resized “thumbnail” version of the image with Pillow
        img.thumbnail(output_size)
        # Find the file name of the image
        img_filename = Path(image.file.name).name
        # Spilt the filename on “.” to get the file extension only
        img_suffix = str(Path(image.file.name).name.split(".")[-1]).lower()
        # Use the file extension to determine the file type from the image_types dictionary
        img_format = image_types[img_suffix]
        # Save the resized image into the buffer, noting the correct file type
        buffer = BytesIO()
        img.save(buffer, format=img_format)
        # Wrap the buffer in File object
        file_object = File(buffer)
        # Save the new resized file as usual, which will save to S3 using django-storages
        image.save(img_filename, file_object)