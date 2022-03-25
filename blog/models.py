from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.shortcuts import render

from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase

from modelcluster.fields import ParentalKey
from wagtail.core.models import Page
from wagtail.core.fields import StreamField, RichTextField
from wagtail.core import blocks
from wagtail.embeds.blocks import EmbedBlock
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, InlinePanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.search import index
from wagtail.contrib.routable_page.models import RoutablePageMixin, route

class BlogIndexPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)

        #Get blogpages
        blogpages = self.get_children().live().order_by('-first_published_at')

        #Filter by tag
        tag = request.GET.get('tag')
        if tag:
            blogpages = blogpages.filter(tags__name=tag)

        context['blogpages'] = blogpages
        return context

class BlogPageTag(TaggedItemBase):
    content_object = ParentalKey('BlogPage', on_delete=models.CASCADE, related_name='tagged_items')

class BlogPage(RoutablePageMixin, Page):
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    date = models.DateTimeField("Post date", default=timezone.now)
    body = StreamField([
        ('heading', blocks.CharBlock(form_classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('quote', blocks.BlockQuoteBlock(help_text="Do not include quote brackets.")),
        ('bedframe', EmbedBlock()),
    ])
    intro = models.TextField(help_text="First 500 Chars of article for Blog Index Page.", max_length=500,)
    tags = ClusterTaggableManager(through=BlogPageTag, blank=True)

    @route(r'^comment/new/$')
    def add_comment_to_post(self, request):
        from .forms import CommentForm

        if request.method == 'POST':
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save()
                return render(request, self.template, {
                    'page': self,
                    'comment': comment,
                })
        else:
            form = CommentForm()

        return render(request, self.template, {
            'page': self,
            'form': form,
        })

    search_fields = Page.search_fields + [
        index.SearchField('body'),
        index.SearchField('comments')
    ]

    content_panels = Page.content_panels + [
        FieldPanel('author'),
        FieldPanel('date'),
        StreamFieldPanel('body'),
        FieldPanel('intro'),
        InlinePanel('comments', label="Comments")
    ]
    promote_panels = Page.promote_panels + [
        FieldPanel('tags'),
    ]

class Comment(models.Model):
    blog_page = models.ForeignKey(BlogPage, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField() 
    date_created = models.DateTimeField(default=timezone.now) 
    date_updated = models.DateTimeField(auto_now=True) 
    active = models.BooleanField(default=True) 

    panels = [
        FieldPanel('body'),
    ]

    class Meta: 
        ordering = ('date_created',) 

    def __str__(self): 
        return 'Comment by {} on {}'.format(self.author.username, self.post)