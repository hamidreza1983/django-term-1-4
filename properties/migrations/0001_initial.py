# Generated by Django 4.2 on 2025-03-17 22:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('root', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Method',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Properties',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image1', models.ImageField(default='default.jpg', upload_to='property')),
                ('image2', models.ImageField(default='default.jpg', upload_to='property')),
                ('image3', models.ImageField(default='default.jpg', upload_to='property')),
                ('title', models.CharField(max_length=150)),
                ('content', models.TextField()),
                ('property_id', models.IntegerField(unique=True)),
                ('location', models.CharField(max_length=150)),
                ('area', models.FloatField()),
                ('beds', models.IntegerField()),
                ('baths', models.IntegerField()),
                ('garage', models.IntegerField()),
                ('price', models.FloatField()),
                ('floor', models.ImageField(default='default.jpg', upload_to='property')),
                ('video', models.TextField()),
                ('map', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='root.agents')),
                ('method', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='properties.method')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='properties.type')),
            ],
        ),
    ]
