# Generated by Django 4.2.15 on 2024-09-17 14:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appname', '0041_alter_hatirlatici_baslangic_tarihi_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='hatirlatici',
            name='is_stopped',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='passwordresetcode',
            name='expires_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 17, 14, 42, 54, 577600, tzinfo=datetime.timezone.utc)),
        ),
    ]
