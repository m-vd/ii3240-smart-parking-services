# Generated by Django 2.1.7 on 2019-04-02 00:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('park', '0003_auto_20190402_0003'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parkrecord',
            name='checkOutTime',
        ),
    ]
