# Generated by Django 3.1.2 on 2021-03-04 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20210301_1618'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='customizeable',
            field=models.BooleanField(default=False),
        ),
    ]
