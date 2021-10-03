from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields.related import ForeignKey

shoe_type_choices = [
    ('sneaker', 'sneaker'),
    ('boot', 'boot'),
    ('sandal', 'sandal'),
    ('dress', 'dress'),
    ('other', 'other')
]

color_name_choices = [
    ('Red', 'Red'),
    ('Orange', 'Orange'),
    ('Yellow', 'Yellow'),
    ('Green', 'Green'),
    ('Blue', 'Blue'),
    ('Indigo', 'Indigo'),
    ('Violet', 'Violet'),
    ('White', 'White'),
    ('Black', 'Black')
]


class Manufacturer(models.Model):
    name = models.CharField(max_length=50)
    website = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name


class ShoeType(models.Model):
    style = models.CharField(
        max_length=20,
        choices=shoe_type_choices,
        default="sneaker"
        )

    def __str__(self):
        return self.style


class ShoeColor(models.Model):
    color_name = models.CharField(
        max_length=20,
        choices=color_name_choices,
        default='Red'
        )

    def __str__(self):
        return self.color_name


class Shoe(models.Model):
    size = models.IntegerField()
    brand_name = models.CharField(max_length=30)
    manufacturer = ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE,
        related_name="made",
        null=True,
        blank=True
        )
    color = ForeignKey(
        ShoeColor,
        on_delete=models.CASCADE,
        related_name='shoecolor',
        null=True,
        blank=True
        )
    material = CharField(max_length=50)
    shoe_type = ForeignKey(
        ShoeType,
        on_delete=models.CASCADE,
        related_name='shoetype',
        null=True,
        blank=True
        )
    fasten_type = CharField(max_length=50)

    def __str__(self):
        return self.brand_name
