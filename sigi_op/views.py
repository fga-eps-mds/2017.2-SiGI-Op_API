from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from ipa.serializers import UserSerializer
from django.contrib.auth.models import User


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
