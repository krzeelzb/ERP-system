# Generated by Django 2.0.9 on 2018-12-09 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_app', '0005_auto_20181209_1410'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderedproducts',
            name='id_order',
        ),
        migrations.AddField(
            model_name='orderedproducts',
            name='id',
            field=models.AutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
