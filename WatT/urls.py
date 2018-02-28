"""WatT URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from wattApp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.login),
    url(r'^about$',views.aboutus),
    url(r'^login$',views.clientspace),
    url(r'^home$', views.home),
    url(r'^add_user$', views.add_user),
    url(r'^create_h/(?P<plant_id>\d+)/(?P<humidity>\d+)/$', views.create_Hmeasure),
    url(r'^create_u/(?P<user_id>\d+)/(?P<humidity>\d+)/(?P<temperature>\d+)/$', views.create_Usermeasure),
    url(r'^get_goal/(?P<plant_id>\d+)/$', views.get_goal),
    url(r'^change_goal$',views.change_goal),
    url(r'^add_plant$', views.add_plant),
    url(r'^history$', views.history)
]
