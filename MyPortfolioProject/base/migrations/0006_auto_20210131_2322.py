# Generated by Django 3.1.5 on 2021-01-31 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_auto_20210131_2149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(blank=True, default='/images/placeholder.png', null=True, upload_to='images'),
        ),
    ]
