# Generated by Django 3.1.2 on 2020-12-08 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financial', '0005_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='time_posted',
            field=models.DateField(auto_now_add=True),
        ),
    ]
