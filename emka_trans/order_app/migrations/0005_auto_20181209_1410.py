# Generated by Django 2.0.9 on 2018-12-09 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_app', '0004_auto_20181209_1407'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkout',
            name='id_checkout',
        ),
        migrations.AddField(
            model_name='checkout',
            name='id',
            field=models.AutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
