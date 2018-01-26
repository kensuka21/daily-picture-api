# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import logout

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from login.serializers import UserSerializer


@api_view(['GET'])
def get_current_user(request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data)


@api_view(['POST'])
def logout_user(request):
    logout(request)
    return Response(status=status.HTTP_200_OK)