# Generated by Django 2.0.9 on 2018-11-26 16:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products_app', '0003_auto_20181102_1702'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='id_deliever',
            new_name='name_deliever',
        ),
    ]
