# Generated by Django 3.2.7 on 2021-09-11 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Law',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('types', models.IntegerField(choices=[(1, 'Type 1'), (2, 'Type 2'), (3, 'Type 3')], max_length=30)),
                ('short_description', models.CharField(max_length=1000)),
                ('full_description', models.TextField()),
            ],
        ),
    ]
