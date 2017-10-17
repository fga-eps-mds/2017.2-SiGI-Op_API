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
from ipa.views import ContactViewSet, ContactTypeViewSet, GeneratorListViewSet
from ipa.views import NoBreakViewSet
from ipa.views import SwitchViewSet
from dgo.views import GODListViewSet
from dgo.views import GODPortListViewSet, GODPortConnectionTypeListViewSet
from gbic.views import GBICListViewSet, GBIC_TypeListViewSet
from emendation_box.views import EmendationBoxListViewSet
from emendation_box.views import EmendationBoxTypeListViewSet
from emendation_box.views import EmendationBoxStructureListViewSet
from post.views import PostListViewSet
from uplink.views import UplinkViewSet
from technical_reserve.views import TechnicalReserveListViewSet
from .views import login, create_auth

router = DefaultRouter()
router.register(r'undergroundboxes', views.UndergroundBoxViewSet)
router.register(r'undergroundboxtypes', views.UndergroundBoxTypeViewSet)
router.register(r'dgos', GODListViewSet, base_name='dgo')
router.register(r'god_ports', GODPortListViewSet, base_name='god_port')
router.register(r'god_port_types', GODPortConnectionTypeListViewSet,
                base_name='god_port_connection')
router.register(r'gbics', GBICListViewSet, base_name='gbic')
router.register(r'gbic_types', GBIC_TypeListViewSet, base_name='gbic_type')
router.register(r'ipas', IpaListViewSet, base_name='ipa')
router.register(r'generators', GeneratorListViewSet, base_name='generator')
router.register(r'ipa-types', IpaTypeListViewSet, base_name='ipatype')
router.register(r'emendation_boxes',
                EmendationBoxListViewSet, base_name='emendation_box')
router.register(r'emendation_box_types',
                EmendationBoxTypeListViewSet, base_name='emendation_type')
router.register(r'emendation_box_structures',
                EmendationBoxStructureListViewSet, base_name='structure')
router.register(r'technicalreserves', TechnicalReserveListViewSet,
                base_name='technical_reserve')
router.register(r'posts', PostListViewSet, base_name='post')
router.register(r'sites', SiteListViewSet, base_name="site")
router.register(r'sitetypes', SiteTypeListViewSet, base_name="sitetype")
router.register(r'nobreaks', NoBreakViewSet, base_name='nobreak')
router.register(r'switches', SwitchViewSet, base_name='switch')
router.register(r'uplinks', UplinkViewSet, base_name='uplink')
router.register(r'contacts', ContactViewSet, base_name="contact")
router.register(r'contacttypes', ContactTypeViewSet, base_name="contacttype")

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^login', login),
    url(r'^users/register', create_auth)
]
