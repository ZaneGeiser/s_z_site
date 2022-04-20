from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager
from django.db.models.signals import pre_save
from s_z_site.utils import unique_slug_generator
from markdownx.models import MarkdownxField
import markdown

# Post Class for Blog Post on Site. Uses Django Database.
class Post(models.Model):
    title = models.CharField(max_length=100)
    body = MarkdownxField(
        help_text="""This Field Supports basic Markdown.
        See <a href='https://www.markdownguide.org/cheat-sheet/' target='blank'>this markdown cheat sheet</a> for help. \n
        This field supports headings, bold, italic, blockquote, ordered list, unordered list, code, fenced code block, 
        horizontal rule, link, image, table, abbreviations, attribute Lists, footnotes, and definition list.
        Image drag and drop is also supported.""")
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = TaggableManager()
    slug = models.SlugField(max_length=100, unique=True)

    def formatted_markdown_body(self):
        return markdown.markdown(text=self.body, extensions=['extra'])

    def body_summary(self):
        return markdown.markdown(text=self.body[:300] + f"...[read more]({self.get_absolute_url()})", extensions=['extra'])

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