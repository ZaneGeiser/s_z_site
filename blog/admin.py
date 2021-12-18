from django.contrib import admin
from .models import Post, Comment

admin.site.register(Post)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'date_created', 'active')
    list_filter = ('active', 'date_created', 'date_updated')
    search_fields = ('author', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)
