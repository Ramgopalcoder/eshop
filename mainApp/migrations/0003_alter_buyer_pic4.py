# Generated by Django 4.1.3 on 2022-11-11 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0002_alter_product_pic1_alter_product_pic2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyer',
            name='pic4',
            field=models.ImageField(blank=True, default='', null=True, upload_to='uploads'),
        ),
    ]