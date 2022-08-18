# Generated by Django 3.2.8 on 2021-10-15 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_auto_20211015_1234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(default=' ', max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='upload/products/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]