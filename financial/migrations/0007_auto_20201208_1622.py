# Generated by Django 3.1.2 on 2020-12-08 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financial', '0006_auto_20201208_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='time_posted',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
