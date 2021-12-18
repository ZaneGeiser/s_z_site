from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Comment

# Create your tests here.
class PostTestCase(TestCase):
    def setUp(self):
        User.objects.create(username='testuser',
        password='testpass', email='test@example.com')
        Post.objects.create(title='This is a Test Title', author_id=1)
        Post.objects.create(title='This is a Test Title', author_id=1)

    def test_check_slugs(self):
        object_1 = Post.objects.get(pk=1)
        object_2 = Post.objects.get(pk=2)
        self.assertEqual(object_1.slug, 'this-is-a-test-title')
        self.assertEqual(object_2.slug, 'this-is-a-test-title-2')

    def test_comment_create(self):
        post_1 = Post.objects.get(pk=1)
        Comment.objects.create(post=post_1, body='a comment on the post.', author_id=1)
        self.assertEqual(post_1.comments.get(id=1).body, 'a comment on the post.' )
        self.assertEqual(post_1.comments.get(id=1).post, post_1 )
        self.assertEqual(post_1.comments.get(id=1).author, User.objects.first() )


