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
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from underground_box import views
from django.contrib import admin
from ipa.views import SiteListViewSet, SiteTypeListViewSet
from ipa.views import  IpaListViewSet, IpaTypeListViewSet
from dgo.views import GODListViewSet

router = DefaultRouter()
router.register(r'undergroundbox', views.UndergroundBoxViewSet)
router.register(r'undergroundboxtype',views.UndergroundBoxTypeViewSet)
router.register(r'dgos', GODListViewSet, base_name='dgo')
router.register(r'ipas', IpaListViewSet, base_name='ipa')
router.register(r'ipas-type', IpaTypeListViewSet, base_name='type')
router.register(r'site', SiteListViewSet, base_name="site")
router.register(r'sitetype', SiteTypeListViewSet, base_name="sitetype")

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^',include('contact.urls'))
]
