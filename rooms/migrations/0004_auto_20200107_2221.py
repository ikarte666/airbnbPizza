# Generated by Django 2.2.5 on 2020-01-07 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0003_auto_20200107_2220'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='facility',
            field=models.ManyToManyField(to='rooms.Facility'),
        ),
        migrations.AddField(
            model_name='room',
            name='houserule',
            field=models.ManyToManyField(to='rooms.HouseRule'),
        ),
        migrations.AlterField(
            model_name='room',
            name='amenities',
            field=models.ManyToManyField(to='rooms.Amenity'),
        ),
    ]
