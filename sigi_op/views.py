from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, viewsets, pagination
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer
from django.db.models import Q, CharField

from emendation_box.models import EmendationBox
from ipa.models import Site
from technical_reserve.models import TechnicalReserve
from underground_box.models import UndergroundBox


@api_view(['POST'])
def create_auth(request):
    serialized = UserSerializer(data=request.data)

    response = 0

    if serialized.is_valid():
        User.objects.create_user(serialized.data['username'],
                                 serialized.data['email'],
                                 serialized.data['password'])
        response = Response({'username': serialized.data['username'],
                             'email': serialized.data['email']},
                            status=status.HTTP_201_CREATED)
    else:
        response = Response(serialized.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    return response


@api_view(['POST'])
def update_auth(request):
    user = User.objects.get(pk=request.data['pk'])
    if user.check_password(request.data['currentpassword']):
        user.username = request.data['username']
        user.email = request.data['email']
        if request.data['password'] != '':
            user.set_password(request.data['password'])
        user.save()
        return Response({'username': user.username,
                        'email': user.email},
                        status=status.HTTP_200_OK)
    else:
        return Response('error', status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username=username, password=password)
    print(user.password)
    if not user:
        return Response({'error', 'Login failed'},
                        status=status.HTTP_401_UNAUTHORIZED)

    token, _ = Token.objects.get_or_create(user=user)
    return Response({
        "username": username,
        "token": token.key,
        "email": user.email,
        "pk": user.pk})


class CustomViewSet(viewsets.ModelViewSet):
    class_name = ""
    order_param_name = ""

    def list(self, request):
        queryset = self.class_name.objects.all().order_by(
            self.order_param_name
            )
        if request.GET.get('search'):
            queryset = []
            param = self.request.query_params.get('search', None)
            if param is not None:
                fieldsChar = [
                    f for f in self.class_name._meta.fields
                    if isinstance(f, CharField)]
                fields = [
                    f for f in self.class_name._meta.fields
                    if not isinstance(f, CharField)]
                queriesChar = [
                    Q(**{f.name+'__contains': param})
                    for f in fieldsChar]
                try:
                    paramNum = int(param)
                except ValueError:
                    paramNum = 0
                queries = [Q(**{f.name: paramNum}) for f in fields]
                print(fields)
                qs = Q()
                for query in queries:
                    qs = qs | query
                for query in queriesChar:
                    qs = qs | query
                queryset = self.class_name.objects.filter(qs)
        if request.GET.get('all'):
            self.pagination_class = None
            serializer = self.serializer_class(  # pylint: disable=not-callable
                queryset,
                many=True)
            response = Response(serializer.data)
        else:
            paginator = pagination.PageNumberPagination()
            queryset = paginator.paginate_queryset(
                queryset=queryset,
                request=request
                )
            serializer = self.serializer_class(  # pylint: disable=not-callable
                queryset,
                many=True)
            response = paginator.get_paginated_response(serializer.data)

        return response


@api_view(['GET'])
def networkmap(_request):
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
