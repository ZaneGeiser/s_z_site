from django.urls import path
from .views import (
    PostDeleteView, PostListView, PostDetailView, 
    PostCreateView, PostUpdateView,
    PostDeleteView)
from . import views

urlpatterns = [
    path('', PostListView.as_view()  , name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),

]
 
# Default PostListView Search Pattern.
# <app>/<model>_<Viewtype>.html
# changed the template_name in ./views.py to match my convetion.
# ie. <app>/<model>.html