# Generated by Django 3.2 on 2021-06-10 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artgallery', '0010_customuser_background_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='bill_number',
            field=models.IntegerField(blank=True, default=1, max_length=16),
            preserve_default=False,
        ),
    ]