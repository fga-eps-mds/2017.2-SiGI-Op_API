from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer
from django.contrib.auth.models import User

from emendation_box.models import EmendationBox
from ipa.models import Site
from technical_reserve.models import TechnicalReserve
from underground_box.models import UndergroundBox


@api_view(['POST'])
def create_auth(request):
    serialized = UserSerializer(data=request.data)

    if serialized.is_valid():
        User.objects.create_user(serialized.data['username'],
                                 serialized.data['email'],
                                 serialized.data['password']
                                 )
        return Response({'username': serialized.data['username'],
                        'email': serialized.data['email']},
                        status=status.HTTP_201_CREATED)
    else:
        return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username=username, password=password)

    if not user:
        return Response({'error', 'Login failed'},
                        status=status.HTTP_401_UNAUTHORIZED)

    token, _ = Token.objects.get_or_create(user=user)
    return Response({"username": username, "token": token.key})


@api_view(['GET'])
def networkmap(request):
    emendation_boxes = []
    for emendation_box in EmendationBox.objects.all():
        emendation_box_dic = {}
        emendation_box_dic['name'] = emendation_box.designNumber
        emendation_box_dic['lattitude'] = emendation_box.lattitude
        emendation_box_dic['longitude'] = emendation_box.longitude
        emendation_boxes.append(emendation_box_dic)

    sites = []
    for site in Site.objects.all():
        site_dic = {}
        site_dic["name"] = site.name
        site_dic["lattitude"] = site.lattitude
        site_dic["longitude"] = site.longitude
        sites.append(site_dic)

    technical_reserves = []
    for technical_reserve in TechnicalReserve.objects.all():
        technical_reserve_dic = {}
        technical_reserve_dic['name'] = technical_reserve.code
        technical_reserve_dic['lattitude'] = technical_reserve.lattitude
        technical_reserve_dic['longitude'] = technical_reserve.longitude
        technical_reserves.append(technical_reserve_dic)

    underground_boxes = []
    for underground_box in UndergroundBox.objects.all():
        underground_box_dic = {}
        underground_box_dic['name'] = underground_box.code
        underground_box_dic['lattitude'] = underground_box.lattitude
        underground_box_dic['longitude'] = underground_box.longitude
        underground_boxes.append(underground_box_dic)

    response = {
        'emendation_box': emendation_boxes,
        'site': sites,
        'technical_reserve': technical_reserves,
        'underground_box': underground_boxes}

    return Response(response)
