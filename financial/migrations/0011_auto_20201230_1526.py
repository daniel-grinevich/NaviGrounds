# Generated by Django 3.1.2 on 2020-12-30 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financial', '0010_auto_20201229_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='receipt_img',
            field=models.FileField(default='default.jpg', upload_to='receipt_pics'),
        ),
    ]
