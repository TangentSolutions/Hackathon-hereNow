# Generated by Django 2.0.3 on 2018-03-16 13:12

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0002_auto_20180316_1300'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='UserDetail',
        ),
    ]