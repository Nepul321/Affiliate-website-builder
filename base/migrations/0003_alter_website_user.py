# Generated by Django 3.2.7 on 2021-10-16 00:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_website_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='website',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='base.user'),
            preserve_default=False,
        ),
    ]
