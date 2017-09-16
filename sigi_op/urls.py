"""sigi_op URL Configuration

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
from django.conf.urls import include,url
from ipa.views import  IpaListViewSet, IpaTypeListViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'ipas', IpaListViewSet, base_name='ipa')
router.register(r'ipas-type', IpaTypeListViewSet, base_name='type')
urlpatterns = [
    #  url(r'^ipas/$', IpaList.as_view()),
    # url(r'^ipas/(?P<pk>[0-9]+)/$', IpaDetail.as_view()),
    url(r'^', include(router.urls)),
]
