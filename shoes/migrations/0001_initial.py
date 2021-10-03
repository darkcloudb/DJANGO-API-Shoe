# Generated by Django 3.2.7 on 2021-09-29 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('website', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ShoeColor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color_name', models.CharField(choices=[('Red', 'Red'), ('Orange', 'Orange'), ('Yellow', 'Yellow'), ('Green', 'Green'), ('Blue', 'Blue'), ('Indigo', 'Indigo'), ('Violet', 'Violet'), ('White', 'White'), ('Black', 'Black')], default='Red', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ShoeType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('style', models.CharField(choices=[('sneaker', 'sneaker'), ('boot', 'boot'), ('sandal', 'sandal'), ('dress', 'dress'), ('other', 'other')], default='sneaker', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Shoe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.IntegerField()),
                ('brand_name', models.CharField(max_length=30)),
                ('material', models.CharField(max_length=50)),
                ('fasten_type', models.CharField(max_length=50)),
                ('color', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shoecolor', to='shoes.shoecolor')),
                ('manufacturer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='manufacturer', to='shoes.manufacturer')),
                ('shoe_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shoetype', to='shoes.shoetype')),
            ],
        ),
    ]