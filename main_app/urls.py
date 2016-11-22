from django.conf.urls import url
from . import views

# create our specific app's url pattern
urlpatterns = [
    url(r'^$', views.index),
]
