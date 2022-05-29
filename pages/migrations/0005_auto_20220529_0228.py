# Generated by Django 3.1.3 on 2022-05-29 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_guiavideos'),
    ]

    operations = [
        migrations.AddField(
            model_name='guiavideos',
            name='video',
            field=models.FileField(null=True, upload_to='videos_uploaded'),
        ),
        migrations.AlterField(
            model_name='guiavideos',
            name='primeiro_texto',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='guiavideos',
            name='segundo_texto',
            field=models.CharField(max_length=250),
        ),
    ]
