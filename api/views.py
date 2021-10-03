from django.db.models.base import Model
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from shoes.models import Manufacturer, ShoeType, ShoeColor, Shoe
from api.serializers import ManufacturerSerializer, ShoeTypeSerializer, ShoeColorSerializer, ShoeSerializer


class ManufacturerViewSet(ModelViewSet):
    serializer_class = ManufacturerSerializer
    queryset = Manufacturer.objects.all()

class ShoeTypeViewSet(ModelViewSet):
    serializer_class = ShoeTypeSerializer
    queryset = ShoeType.objects.all()

class ShoeColorViewSet(ModelViewSet):
    serializer_class = ShoeColorSerializer
    queryset = ShoeColor.objects.all()

class ShoeViewSet(ModelViewSet):
    serializer_class = ShoeSerializer
    queryset = Shoe.objects.all()

    # @action(methods=['get'], detail=False)
    # def newshoe(self, request):
    #     new = self.get_queryset().ordered_by('size')
    #     serializer = self.get_serializer_class()(new)
    #     return Response(serializer.data)

# Create your views here.
