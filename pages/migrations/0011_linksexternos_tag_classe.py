# Generated by Django 3.1.3 on 2022-06-07 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0010_linksexternos'),
    ]

    operations = [
        migrations.AddField(
            model_name='linksexternos',
            name='tag_classe',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
    ]
