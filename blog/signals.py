from django.dispatch import receiver
from django.db.models import signals
from .models import Post, Comment
from django.contrib.auth.models import User
from django.template.loader import render_to_string

@receiver(signals.post_save, sender=Post)
def send_newpost_email_notification(sender, instance, created, **kwargs):
    if created:
        print('signal email')
        subject = f"New Blog Post from {instance.author.get_full_name()}"
        msg_plain = render_to_string('blog/new_post_email.txt',
            {'post_body_summary': f"{instance.body[:500]}...",
            'post_title': instance.title,
            'post_url': instance.get_absolute_url(),
            'site_url': "https://s-z-site.herokuapp.com/"})
        msg_html = render_to_string('blog/new_post_email.html',
            {'post_body_summary': f"{instance.body[:500]}...",
            'post_title': instance.title,
            'post_url': instance.get_absolute_url(),
            'site_url': 'https://s-z-site.herokuapp.com/'})
        for user in User.objects.all():
            if user.username == 'zanegeiser':
                user.email_user(subject, message=msg_plain, html_message=msg_html)