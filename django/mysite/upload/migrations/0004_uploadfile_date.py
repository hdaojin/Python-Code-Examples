# Generated by Django 3.2.11 on 2022-01-19 15:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0003_auto_20220119_2252'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadfile',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
