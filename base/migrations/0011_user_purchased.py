# Generated by Django 3.2.7 on 2021-10-23 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_product_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='purchased',
            field=models.BooleanField(default=False),
        ),
    ]
