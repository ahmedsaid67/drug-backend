# Generated by Django 4.2.15 on 2024-09-12 10:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appname', '0030_remove_hastalikhemyasahemkiloyabagliazalandoz_maksimum_anlik_doz_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hastalikazalankilodoz',
            name='maksimum_anlik_doz',
        ),
        migrations.RemoveField(
            model_name='hastalikazalankilodoz',
            name='maksimum_gunluk_doz',
        ),
        migrations.AlterField(
            model_name='passwordresetcode',
            name='expires_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 12, 10, 42, 28, 43284, tzinfo=datetime.timezone.utc)),
        ),
    ]
