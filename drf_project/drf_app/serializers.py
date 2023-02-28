from rest_framework import serializers
from .models import Image


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        #extra_kwargs = {'url': {'write_only': True}}
        fields = ['id', 'url', 'title', 'width', 'height']
        read_only_fields = ['id']
