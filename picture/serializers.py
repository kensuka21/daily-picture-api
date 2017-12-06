from rest_framework.serializers import ModelSerializer

from login.serializers import UserSerializer
from models import *


class PictureSerializer(ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Picture
        fields = '__all__'


