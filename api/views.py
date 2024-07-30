from rest_framework import viewsets, mixins
from .models import Pereval
from .serializers import *
from rest_framework.response import Response


class ImageViewSet(viewsets.ModelViewSet):
    queryset = PerevalImages.objects.all()
    serializer_class = ImageSerializer


class CoordViewSet(viewsets.ModelViewSet):
    queryset = PerevalCoords.objects.all()
    serializer_class = CoordsSerializer


class LevelViewSet(viewsets.ModelViewSet):
    queryset = PerevalLevels.objects.all()
    serializer_class = LevelSerializer


class PerevalViewSet(viewsets.ModelViewSet):
    queryset = Pereval.objects.all()
    serializer_class = PerevalSerializer

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.status == "new":
            if "user" in request.data:
                del request.data["user"]
            super().partial_update(request, *args, **kwargs)
            return Response({"state": 1, "message": "Record updated successfully"})
        return Response({"state": 0, "message": "Cannot update a completed pereval"})


class PerevalEmailViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Pereval.objects.all()
    serializer_class = PerevalSerializer

    def list(self, request, *args, **kwargs):
        email = request.query_params.get("user__email", None)
        if email:
            queryset = self.filter_queryset(
                self.get_queryset().filter(user__email=email)
            )
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        else:
            return Response({"error": "Missing user__email parameter"})
