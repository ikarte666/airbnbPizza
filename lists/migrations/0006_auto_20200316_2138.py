# Generated by Django 2.2.5 on 2020-03-16 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0005_auto_20200316_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='name',
            field=models.CharField(max_length=80, null=True),
        ),
    ]
