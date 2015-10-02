from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^accounts/login/$', views.login, name='login'),
    url(r'^accounts/$', views.profile, name='profile'),
    url(r'^accounts/register/$', views.register, name='register'),
    url(r'^account/register_success/$', views.register_success, name='register_success'),
    url(r'^accounts/logout/$', views.logout, name='logout'),
    url(r'^all-news/$', views.news, name='news'),
    url(r'^C.O.G-Talents/$', views.talents, name='talents'),
    url(r'^C.O.G-Talk/$', views.talk, name='talk'),
    url(r'^about/$', views.about, name='about'),
    # url(r'^get/(?P<article_id>[0-9]+)/$', views.article, name='article'),
    # url(r'^media/$', views.media, name='media'),
]