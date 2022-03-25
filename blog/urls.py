from django.urls import path, include
from wagtail.core import urls as wagtail_urls

urlpatterns = [
   path('', include(wagtail_urls)),

]
 
# Default PostListView Search Pattern.
# <app>/<model>_<Viewtype>.html
# changed the template_name in ./views.py to match my convetion.
# ie. <app>/<model>.html