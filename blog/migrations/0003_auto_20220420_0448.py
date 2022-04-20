# Generated by Django 3.2.6 on 2022-04-20 04:48

from django.db import migrations
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_body'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='content',
        ),
        migrations.AlterField(
            model_name='post',
            name='body',
            field=markdownx.models.MarkdownxField(help_text="This Field Supports basic Markdown.\n        See <a href='https://www.markdownguide.org/cheat-sheet/' target='blank'>this markdown cheat sheet</a> for help. \n\n        This field supports headings, bold, italic, blockquote, ordered list, unordered list, code, fenced code block, \n        horizontal rule, link, image, table, abbreviations, attribute Lists, footnotes, and definition list.\n        Image drag and drop is also supported."),
        ),
    ]