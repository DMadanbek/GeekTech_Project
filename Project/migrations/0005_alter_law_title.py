# Generated by Django 3.2.7 on 2021-09-16 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0004_auto_20210916_0910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='law',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
