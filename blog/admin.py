from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import Post, Comment

@admin.register(Post)
class PostAdmin(MarkdownxModelAdmin):
    list_display = ('title', 'date_posted', 'author')
    list_filter = ('date_posted', 'tags')
    search_fields = ('title', 'body')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'date_created', 'active')
    list_filter = ('active', 'date_created', 'date_updated')
    search_fields = ('author', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)
