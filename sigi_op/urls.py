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
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from underground_box import views
from ipa.views import SiteListViewSet, SiteTypeListViewSet
from ipa.views import IpaListViewSet, IpaTypeListViewSet
from ipa.views import ContactViewSet, ContactTypeViewSet
from dgo.views import GODListViewSet
from segments.views import SegmentViewSet
from emendation_box.views import EmendationBoxListViewSet
from emendation_box.views import EmendationBoxTypeListViewSet
from emendation_box.views import EmendationBoxStructureListViewSet
from uplink.views import UplinkViewSet
from technical_reserve.views import TechnicalReserveListViewSet
from .views import login, create_auth


router = DefaultRouter()
router.register(r'undergroundbox', views.UndergroundBoxViewSet)
router.register(r'undergroundboxtype', views.UndergroundBoxTypeViewSet)
router.register(r'dgos', GODListViewSet, base_name='dgo')
router.register(r'ipas', IpaListViewSet, base_name='ipa')
router.register(r'ipas-type', IpaTypeListViewSet, base_name='type')
router.register(r'emendation_box',
                EmendationBoxListViewSet, base_name='emendation_box')
router.register(r'emendation_box_type',
                EmendationBoxTypeListViewSet, base_name='type')
router.register(r'emendation_box_structure',
                EmendationBoxStructureListViewSet, base_name='structure')
router.register(r'technicalreserves', TechnicalReserveListViewSet,
                base_name='technical_reserve')
router.register(r'site', SiteListViewSet, base_name="site")
router.register(r'sitetype', SiteTypeListViewSet, base_name="sitetype")
router.register(r'uplink', UplinkViewSet, base_name='uplink')
router.register(r'contact', ContactViewSet, base_name="contact")
router.register(r'contacttype', ContactTypeViewSet, base_name="contacttype")
router.register(r'segments', SegmentViewSet, base_name="segment")

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^login', login),
    url(r'^users/register', create_auth)
]
