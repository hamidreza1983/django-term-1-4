# Generated by Django 5.1.1 on 2024-11-28 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0005_alter_properties_map_alter_properties_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='properties',
            name='map',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='properties',
            name='video',
            field=models.TextField(),
        ),
    ]