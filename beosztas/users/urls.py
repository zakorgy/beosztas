from django.conf.urls import url

from . import views

app_name= 'users'
urlpatterns = [
    url(r'signup/$', views.signup, name='signup'),
    url(r'(?P<user_id>[0-9]+)/add_request/$', views.add_request, name='add_request'),
]