# Generated by Django 2.0.9 on 2018-11-26 16:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products_app', '0004_auto_20181126_1619'),
        ('order_app', '0002_auto_20181102_1748'),
    ]

    operations = [
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('id_checkout', models.IntegerField(primary_key=True, serialize=False)),
                ('name_client', models.CharField(max_length=256)),
                ('price', models.IntegerField()),
                ('weigth', models.IntegerField()),
                ('route_client', models.BooleanField(default=False)),
                ('date', models.DateField()),
                ('magazine', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='OrderedProducts',
            fields=[
                ('id_order', models.IntegerField(primary_key=True, serialize=False)),
                ('id_checkout', models.IntegerField()),
                ('name_deliver', models.CharField(max_length=256)),
                ('amount', models.IntegerField()),
                ('route', models.BooleanField(default=False)),
                ('id_route', models.IntegerField()),
                ('magazine', models.BooleanField(default=False)),
                ('name_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products_app.Product')),
            ],
        ),
    ]
