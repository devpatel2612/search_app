# Generated by Django 3.1 on 2022-04-25 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchbar', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='videofile',
            field=models.FileField(upload_to='videos/'),
        ),
    ]
