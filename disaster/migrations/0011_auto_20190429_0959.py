# Generated by Django 2.1.7 on 2019-04-29 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disaster', '0010_auto_20190428_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disaster',
            name='location',
            field=models.ManyToManyField(blank=True, to='parkingLot.Lot'),
        ),
    ]
