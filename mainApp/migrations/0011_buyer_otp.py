# Generated by Django 4.1.3 on 2023-03-17 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0010_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyer',
            name='otp',
            field=models.IntegerField(default=-1151515),
        ),
    ]