# Generated by Django 2.0.7 on 2019-04-28 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disaster', '0010_auto_20190428_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disaster',
            name='description',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='disaster',
            name='location',
            field=models.ManyToManyField(blank=True, to='parkingLot.Lot'),
        ),
    ]
