from django.conf.urls import url

from . import views

app_name= 'users'
urlpatterns = [
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^add_request/$', views.add_request, name='add_request'),
    url(r'^weekly_shift/$', views.weekly_shift, name='weekly_shift'),
]