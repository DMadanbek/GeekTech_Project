# Generated by Django 3.2.7 on 2021-09-04 13:35

import Project.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('publication_date', models.DateTimeField(auto_now=True)),
                ('short_description', models.CharField(max_length=1000)),
                ('full_description', models.TextField()),
                ('link', models.URLField(blank=True, null=True)),
                ('image', models.ImageField(upload_to=Project.models.upload_to)),
            ],
        ),
        migrations.CreateModel(
            name='ImageNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=Project.models.upload_to)),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='Project.news')),
            ],
        ),
        migrations.CreateModel(
            name='FavouriteNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Project.news')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]