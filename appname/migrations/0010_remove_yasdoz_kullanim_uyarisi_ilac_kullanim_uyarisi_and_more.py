# Generated by Django 4.2.15 on 2024-09-07 13:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appname', '0009_alter_passwordresetcode_expires_at_yasdoz'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='yasdoz',
            name='kullanim_uyarisi',
        ),
        migrations.AddField(
            model_name='ilac',
            name='kullanim_uyarisi',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='passwordresetcode',
            name='expires_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 7, 13, 56, 58, 833209, tzinfo=datetime.timezone.utc)),
        ),
    ]
