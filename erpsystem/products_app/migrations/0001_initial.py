# Generated by Django 2.0.9 on 2018-11-02 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('genre', models.CharField(max_length=256)),
                ('id_deliever', models.CharField(max_length=256)),
                ('amount', models.IntegerField()),
            ],
        ),
    ]
