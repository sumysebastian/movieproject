# Generated by Django 4.1.7 on 2023-03-01 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default='ddffgg', upload_to='gallery'),
            preserve_default=False,
        ),
    ]
