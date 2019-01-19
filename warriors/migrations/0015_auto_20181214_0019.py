# Generated by Django 2.1.3 on 2018-12-13 20:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('warriors', '0014_auto_20181213_2357'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='report',
            options={'verbose_name': 'Report', 'verbose_name_plural': 'Reports'},
        ),
        migrations.AlterModelOptions(
            name='soldier',
            options={'verbose_name': 'Soldier', 'verbose_name_plural': 'Soldiers'},
        ),
        migrations.AlterField(
            model_name='soldier',
            name='report',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='warriors.Report', verbose_name='Report'),
        ),
    ]