from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer 
from rest_framework.serializers import StringRelatedField, PrimaryKeyRelatedField
from shoes.models import Manufacturer, ShoeType, ShoeColor, Shoe


class ManufacturerSerializer(ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = [
            'name',
            'website'
        ]


class ShoeTypeSerializer(ModelSerializer):
    class Meta:
        model = ShoeType
        fields = [
            'style'
        ]


class ShoeColorSerializer(ModelSerializer):
    class Meta:
        model = ShoeColor
        fields = [
            'color_name'
        ]


class ShoeSerializer(HyperlinkedModelSerializer):
    manufacturer = StringRelatedField()
    color = StringRelatedField()
    shoe_type = StringRelatedField()

    class Meta:
        model = Shoe
        fields = [
            'size',
            'brand_name',
            'manufacturer',
            'color',
            'material',
            'shoe_type',
            'fasten_type'
        ]
