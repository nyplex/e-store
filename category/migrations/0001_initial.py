# Generated by Django 3.2.7 on 2021-09-23 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField(max_length=150, unique=True)),
                ('description', models.CharField(blank=True, max_length=500)),
                ('image', models.ImageField(blank=True, upload_to='images/categories')),
            ],
        ),
    ]
