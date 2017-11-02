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
    emendation_box = {
        'latitude': [emendation_box.lattitude for emendation_box in EmendationBox.objects.all()],
        'longitude': [emendation_box.longitude for emendation_box in EmendationBox.objects.all()],
    }
    sites = {
        'latitude': [site.lattitude for site in Site.objects.all()],
        'longitude': [site.longitude for site in Site.objects.all()],
    }
    technical_reserves = {
        'latitude': [technical_reserve.lattitude for technical_reserve in TechnicalReserve.objects.all()],
        'longitude': [technical_reserve.longitude for technical_reserve in TechnicalReserve.objects.all()],
    }
    underground_boxes = {
        'latitude': [underground_box.lattitude for underground_box in UndergroundBox.objects.all()],
        'longitude': [underground_box.longitude for underground_box in UndergroundBox.objects.all()],
    }

    response = {'emendation_box': emendation_box, 'site': sites, 'technical_reserve': technical_reserves, 'underground_box': underground_boxes}

    return Response(response)
