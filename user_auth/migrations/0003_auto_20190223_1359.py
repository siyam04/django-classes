# Generated by Django 2.0.5 on 2019-02-23 07:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0002_auto_20190221_2349'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='profile_img',
            new_name='profile_image',
        ),
    ]
