# Generated by Django 4.2.15 on 2024-08-29 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appname', '0003_alter_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='photo'),
        ),
    ]
