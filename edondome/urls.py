"""edondome URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from app import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('', include('social_django.urls', namespace='social')),
    url(r'^$', view=views.IndexView.as_view(), name='index'),
    url(r'^delete/$', view=views.delete, name='delete'),
    url(r'^logout/$', view=views.logout_user, name='logout'),
    url(r'^comments/$', view=views.comments, name='comments'),
    url(r'^complaint/(?P<pk>[0-9]+)/$', view=views.single, name='view')
]
urlpatterns += staticfiles_urlpatterns()