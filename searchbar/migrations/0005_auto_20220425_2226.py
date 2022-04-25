# Generated by Django 3.1 on 2022-04-25 16:56

from django.db import migrations, models
import searchbar.validators


class Migration(migrations.Migration):

    dependencies = [
        ('searchbar', '0004_auto_20220425_2224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='videofile',
            field=models.FileField(upload_to='videos/', validators=[searchbar.validators.validate_video]),
        ),
    ]
