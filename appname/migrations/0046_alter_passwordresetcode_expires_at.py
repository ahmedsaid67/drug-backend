# Generated by Django 4.2.15 on 2024-09-24 14:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appname', '0045_hatirlaticisaati_is_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passwordresetcode',
            name='expires_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 24, 14, 51, 46, 876867, tzinfo=datetime.timezone.utc)),
        ),
    ]
