# Generated by Django 2.1.7 on 2019-04-29 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parkingLot', '0004_auto_20190429_1315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lot',
            name='lotID',
            field=models.UUIDField(primary_key=True, serialize=False, unique=True),
        ),
    ]
