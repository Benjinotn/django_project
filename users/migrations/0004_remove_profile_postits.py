# Generated by Django 2.2.12 on 2020-06-16 13:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200614_1629'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='postits',
        ),
    ]