# Generated by Django 4.1.6 on 2023-03-21 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HBAPP', '0002_customeroderdetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='customeroderdetails',
            name='hotelid',
            field=models.IntegerField(default=0),
        ),
    ]
