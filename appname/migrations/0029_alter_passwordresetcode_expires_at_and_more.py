# Generated by Django 4.2.15 on 2024-09-11 16:46

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appname', '0028_alter_passwordresetcode_expires_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passwordresetcode',
            name='expires_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 11, 17, 1, 46, 704504, tzinfo=datetime.timezone.utc)),
        ),
        migrations.CreateModel(
            name='HastalikHemYasaHemKiloyaBagliAzalanDoz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kullanim_sikligi', models.CharField(blank=True, max_length=150, null=True)),
                ('check_uyari', models.TextField(blank=True, null=True)),
                ('tipik_min_doz', models.DecimalField(blank=True, decimal_places=4, max_digits=7, null=True)),
                ('tipik_max_doz', models.DecimalField(blank=True, decimal_places=4, max_digits=7, null=True)),
                ('maksimum_anlik_doz', models.DecimalField(blank=True, decimal_places=4, max_digits=8, null=True)),
                ('maksimum_gunluk_doz', models.CharField(blank=True, max_length=150, null=True)),
                ('threshold_age', models.IntegerField()),
                ('threshold_age_min_dose', models.DecimalField(blank=True, decimal_places=4, max_digits=7, null=True)),
                ('threshold_age_max_dose', models.DecimalField(blank=True, decimal_places=4, max_digits=7, null=True)),
                ('hastaliklar', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='hastalikhemyasahemkiloyabagliazalandoz', to='appname.hastalik')),
                ('ilac', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='appname.ilac')),
            ],
        ),
    ]
