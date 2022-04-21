from django.urls import path
from .views import PostListView, PostDetailCommentView, UserPostListView
from . import views

urlpatterns = [
    path('blog/', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<slug:slug>/', PostDetailCommentView.as_view(), name='post-detail'),
    path('about/', views.about, name='blog-about'),
    path('contact/', views.contact, name='blog-contact'),
    path('', views.site_home, name='site-home'),
]

# Default PostListView Search Pattern.
# <app>/<model>_<Viewtype>.html
# changed the template_name in ./views.py to match my convetion.
# ie. <app>/<model>.html
