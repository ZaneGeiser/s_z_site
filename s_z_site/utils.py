from django.utils.text import slugify

#known issue. Will break if multiple users submit articles simulateously.
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