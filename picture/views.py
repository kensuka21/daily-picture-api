# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.files.storage import FileSystemStorage
from django.db import transaction
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from models import *
from picture.serializers import *


class UserViewSet(viewsets.ViewSet):

    def list(self, request):
        pictures = Picture.objects.filter(user=request.user)
        serializer = PictureSerializer(pictures, many=True)
        return Response(serializer.data)


@api_view(['POST'])
@transaction.atomic
def upload_picture(request):
    fs = FileSystemStorage()
    file = request.FILES['file']
    file_name = 'pictures_uploaded/' + file.name

    picture = Picture(path_url=file_name,
                      user=request.user,
                      created_by=request.user.username)
    picture.save()

    uploaded_file = fs.save(file_name, file)

    serializer = PictureSerializer(picture)

    return Response(serializer.data)
