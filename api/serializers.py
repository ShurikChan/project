from rest_framework import serializers
from .models import Pereval, PerevalCoords, PerevalLevels, PerevalImages, PerevalUsers
from drf_writable_nested import WritableNestedModelSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerevalUsers
        fields = '__all__'

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerevalImages
        fields = '__all__'


class CoordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerevalCoords
        fields = '__all__'


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerevalLevels
        fields = '__all__'


class PerevalSerializer(WritableNestedModelSerializer):
    add_time = serializers.DateTimeField(read_only=True)
    image = ImageSerializer(many=True, required=False)
    coord = CoordsSerializer()
    level = LevelSerializer(allow_null = True)
    user = UserSerializer()
    
    class Meta:
        model = Pereval
        fields = ['beautyTitle', 'title', 'other_titles', 'user', 'coord', 'image', 'level', 'add_time']
