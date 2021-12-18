from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager
from django.db.models.signals import pre_save
from s_z_site.utils import unique_slug_generator 

# Post Class for Blog Post on Site. Uses Django Database.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = TaggableManager()
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.slug

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'slug' : self.slug})

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField() 
    date_created = models.DateTimeField(default=timezone.now) 
    date_updated = models.DateTimeField(auto_now=True) 
    active = models.BooleanField(default=True) 

    class Meta: 
        ordering = ('date_created',) 

    def __str__(self): 
        return 'Comment by {} on {}'.format(self.author.username, self.post)

def slug_save(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
    
pre_save.connect(slug_save, sender=Post)