# Generated by Django 2.0.7 on 2019-05-04 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ticketing', '0023_auto_20190503_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parkingLot.Lot'),
        ),
    ]
