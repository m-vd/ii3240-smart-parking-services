# Generated by Django 2.1.7 on 2019-04-29 09:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ticketing', '0012_auto_20190428_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parkingLot.Lot'),
        ),
    ]
