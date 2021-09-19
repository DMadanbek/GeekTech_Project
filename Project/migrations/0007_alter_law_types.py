# Generated by Django 3.2.7 on 2021-09-19 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0006_alter_law_types'),
    ]

    operations = [
        migrations.AlterField(
            model_name='law',
            name='types',
            field=models.CharField(choices=[(1, 'Type 1'), (2, 'Type 2'), (3, 'Type 3')], max_length=30),
        ),
    ]
