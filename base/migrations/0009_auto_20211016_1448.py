# Generated by Django 3.2.7 on 2021-10-16 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_auto_20211016_1444'),
    ]

    operations = [
        migrations.AddField(
            model_name='website',
            name='image1',
            field=models.ImageField(default='', upload_to='carousel/'),
        ),
        migrations.AddField(
            model_name='website',
            name='image2',
            field=models.ImageField(default='', upload_to='carousel/'),
        ),
        migrations.AddField(
            model_name='website',
            name='image3',
            field=models.ImageField(default='', upload_to='carousel/'),
        ),
    ]
