# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.files.storage import FileSystemStorage
from django.db import transaction
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from models import *
from picture.serializers import *


class PictureViewSet(viewsets.ViewSet):

    def list(self, request):
        pictures = Picture.objects.filter(user=request.user).order_by('-id')
        serializer = PictureSerializer(pictures, many=True)
        return Response(serializer.data)


@api_view(['post'])
@transaction.atomic
def upload_picture(request):
    fs = FileSystemStorage()
    file = request.FILES['file']
    caption = request.POST['caption']
    file_name = 'static/' + file.name

    picture = Picture(path_url=file_name,
                      caption=caption,
                      user=request.user,
                      created_by=request.user.username)
    picture.save()

    fs.save(file_name, file)

    serializer = PictureSerializer(picture)

    return Response(serializer.data)


@api_view(['get'])
def get_daily_picture(request):
    picture = Picture.get_daily_picture(request.user)
    serializer = PictureSerializer(picture)

    return Response(serializer.data)
