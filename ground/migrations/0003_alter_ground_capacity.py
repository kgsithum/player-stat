# Generated by Django 4.1.3 on 2022-11-24 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ground', '0002_alter_ground_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ground',
            name='capacity',
            field=models.IntegerField(),
        ),
    ]
