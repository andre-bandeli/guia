# Generated by Django 3.1.3 on 2022-06-07 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0009_auto_20220605_1849'),
    ]

    operations = [
        migrations.CreateModel(
            name='LinksExternos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(max_length=150)),
                ('link', models.CharField(max_length=350)),
            ],
        ),
    ]