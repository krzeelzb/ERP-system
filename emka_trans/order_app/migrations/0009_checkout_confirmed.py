# Generated by Django 2.0.9 on 2018-12-09 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_app', '0008_auto_20181209_1801'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkout',
            name='confirmed',
            field=models.BooleanField(default=False),
        ),
    ]
