# Generated by Django 4.2.15 on 2024-09-26 16:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appname', '0052_alter_ilac_etken_madde_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passwordresetcode',
            name='expires_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 26, 16, 46, 33, 796441, tzinfo=datetime.timezone.utc)),
        ),
    ]
