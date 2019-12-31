from django.conf.urls import url
from . import views

app_name = 'Post'
urlpatterns = [
    url(r'^$', views.all_posts, name='all_posts'),
    url(r'^(?P<id>\d+)$', views.post, name='post'),
    url(r'^create_post$', views.create_post, name='create_post'),
]