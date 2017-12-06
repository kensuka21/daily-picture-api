from rest_framework import serializers
from rest_framework.response import Response


class ExceptionSerializer(serializers.Serializer):
    error = serializers.CharField(max_length=255)


def custom_exception_handler(exc, context):
    serializer = ExceptionSerializer(data={'error': str(exc)})
    serializer.is_valid()
    response = Response(serializer.data, status=403)

    return response