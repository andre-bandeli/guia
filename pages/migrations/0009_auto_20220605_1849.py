# Generated by Django 3.1.3 on 2022-06-05 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_auto_20220605_1824'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guiavideos',
            name='video',
        ),
        migrations.AddField(
            model_name='guiavideos',
            name='link',
            field=models.TextField(default=1, max_length=400),
            preserve_default=False,
        ),
    ]