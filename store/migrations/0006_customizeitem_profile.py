# Generated by Django 3.1.2 on 2021-03-08 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_customizeitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='customizeitem',
            name='profile',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
