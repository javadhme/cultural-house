# Generated by Django 2.1.3 on 2018-12-13 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warriors', '0008_auto_20181213_2352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='photographer_address',
            field=models.CharField(max_length=255, verbose_name='Photographer address'),
        ),
    ]
