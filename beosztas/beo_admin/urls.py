from django.conf.urls import url

from . import views

app_name= 'beo_admin'
urlpatterns = [
    url(r'^create_shifts/$', views.create_shifts, name='create_shifts'),
    url(r'^finalize_shifts/$', views.finalize_shifts, name='finalize_shifts'),
    url(r'^manage_users/$', views.manage_users, name='manage_users'),
    url(r'^last_month_stat/$', views.last_month_stat, name='last_month_stat'),
]