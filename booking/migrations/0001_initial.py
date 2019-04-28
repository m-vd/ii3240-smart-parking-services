# Generated by Django 2.0.7 on 2019-04-28 13:32

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('bookingID', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('userID', models.CharField(max_length=30)),
                ('bookingTime', models.DateTimeField(auto_now_add=True)),
                ('location', models.CharField(max_length=30)),
                ('status', models.CharField(max_length=30)),
            ],
        ),
    ]
