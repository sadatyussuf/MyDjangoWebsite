# Generated by Django 3.1.2 on 2020-12-07 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20201207_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='thumb',
            field=models.ImageField(blank=True, default='images/4.jpg', null=True, upload_to='images/'),
        ),
    ]
