# Generated by Django 4.1.3 on 2022-11-15 19:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0003_alter_buyer_pic4'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='dicount',
            new_name='discount',
        ),
    ]
