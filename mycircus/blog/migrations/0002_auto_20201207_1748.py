# Generated by Django 3.1.2 on 2020-12-07 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='thumb',
            field=models.ImageField(blank=True, default='', null=True, upload_to='images/'),
        ),
    ]
