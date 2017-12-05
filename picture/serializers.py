from rest_framework.serializers import ModelSerializer
from models import *


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class PictureSerializer(ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Picture
        fields = '__all__'


