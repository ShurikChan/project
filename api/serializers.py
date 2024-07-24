from rest_framework import serializers
from .models import Pereval, PerevalCoords, PerevalLevels, PerevalImages, PerevalUsers
from drf_writable_nested import WritableNestedModelSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerevalUsers
        fields = "__all__"


class ImageSerializer(serializers.ModelSerializer):
    data = serializers.CharField()

    class Meta:
        model = PerevalImages
        fields = "__all__"


class CoordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerevalCoords
        fields = "__all__"


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerevalLevels
        fields = "__all__"


class PerevalSerializer(WritableNestedModelSerializer):
    add_time = serializers.DateTimeField(read_only=True, format="%d-%m-%Y %H:%M:%S")
    coords = CoordsSerializer()
    level = LevelSerializer(allow_null=True)
    user = UserSerializer()
    images = ImageSerializer(many=True, source="perevalimages_set")

    class Meta:
        model = Pereval
        fields = [
            "beauty_title",
            "title",
            "other_titles",
            "connect",
            "add_time",
            "user",
            "coords",
            "level",
            "images",
        ]
