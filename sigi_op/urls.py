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
from ipa.views import UserViewSet, GroupViewSet, PermissionViewSet
from ipa.views import SlotViewSet
from ipa.views import SlotPortViewSet
from dgo.views import GODListViewSet, JumperViewSet, AccessCableListViewSet
from dgo.views import GODPortListViewSet, GODPortConnectionTypeListViewSet
from gbic.views import GBICListViewSet, GBICTypeListViewSet
from emendation_box.views import EmendationBoxListViewSet
from emendation_box.views import EmendationBoxTypeListViewSet
from emendation_box.views import EmendationBoxStructureListViewSet
from emendation_box.views import PostListViewSet
from uplink.views import UplinkViewSet
from uplink.views import SegmentsListViewSet
from cable_stretch.views import CableStretchListViewSet
from cable_stretch.views import CableStretchTypeListViewSet
from cable_stretch.views import TubelooseListViewSet
from technical_reserve.views import TechnicalReserveListViewSet
from .views import login, create_auth, networkmap, update_auth
from dgo.views import GODFabricantListViewSet, GODFabricantModelListViewSet


ROUTER = DefaultRouter()
ROUTER.register(r'permissions', PermissionViewSet, base_name='permissions')
ROUTER.register(r'users', UserViewSet, base_name='users')
ROUTER.register(r'groups', GroupViewSet, base_name='groups')
ROUTER.register(r'undergroundboxes', views.UndergroundBoxViewSet)
ROUTER.register(r'undergroundboxtypes', views.UndergroundBoxTypeViewSet)
ROUTER.register(r'dgos', GODListViewSet, base_name='dgo')
ROUTER.register(r'god_ports', GODPortListViewSet, base_name='god_port')
ROUTER.register(r'god_port_types', GODPortConnectionTypeListViewSet,
                base_name='god_port_connection')
ROUTER.register(r'gbics', GBICListViewSet, base_name='gbic')
ROUTER.register(r'gbic_types', GBICTypeListViewSet, base_name='gbic_type')
ROUTER.register(r'ipas', IpaListViewSet, base_name='ipa')
ROUTER.register(r'generators', GeneratorListViewSet, base_name='generator')
ROUTER.register(r'ipa-types', IpaTypeListViewSet, base_name='ipatype')
ROUTER.register(r'emendation_boxes',
                EmendationBoxListViewSet, base_name='emendation_box')
ROUTER.register(r'emendation_box_types',
                EmendationBoxTypeListViewSet, base_name='emendation_type')
ROUTER.register(r'emendation_box_structures',
                EmendationBoxStructureListViewSet, base_name='structure')
ROUTER.register(r'technicalreserves', TechnicalReserveListViewSet,
                base_name='technical_reserve')
ROUTER.register(r'posts', PostListViewSet, base_name='post')
ROUTER.register(r'sites', SiteListViewSet, base_name="site")
ROUTER.register(r'sitetypes', SiteTypeListViewSet, base_name="sitetype")
ROUTER.register(r'nobreaks', NoBreakViewSet, base_name='nobreak')
ROUTER.register(r'switches', SwitchViewSet, base_name='switch')
ROUTER.register(r'slots', SlotViewSet, base_name='slot')
ROUTER.register(r'slotports', SlotPortViewSet, base_name='slotport')
ROUTER.register(r'uplinks', UplinkViewSet, base_name='uplink')
ROUTER.register(r'contacts', ContactViewSet, base_name="contact")
ROUTER.register(r'contacttypes', ContactTypeViewSet, base_name="contacttype")
ROUTER.register(r'access-cables', AccessCableListViewSet,
                base_name="accesscables")
ROUTER.register(r'jumpers', JumperViewSet, base_name='jumper')
ROUTER.register(r'cable_stretches', CableStretchListViewSet,
                base_name='cablestretch')
ROUTER.register(r'cable_stretch_types', CableStretchTypeListViewSet,
                base_name='cablestretchtype')
ROUTER.register(r'tubelooses', TubelooseListViewSet,
                base_name='tubeloose')
ROUTER.register(r'segments', SegmentsListViewSet, base_name='segments')
ROUTER.register(r'god_fabricants', GODFabricantListViewSet,
                base_name='godfabricant')
ROUTER.register(r'god_fabricant_models', GODFabricantModelListViewSet,
                base_name='godfabricantmodel')


urlpatterns = [  # pylint: disable=invalid-name
    url(r'^', include(ROUTER.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^login', login),
    url(r'^users/register', create_auth),
    url(r'^users/update', update_auth),
    url(r'^networkmap/', networkmap),
]
