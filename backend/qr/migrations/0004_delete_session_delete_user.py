# Generated by Django 4.0.4 on 2022-05-28 23:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qr', '0003_user_authtype'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Session',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
