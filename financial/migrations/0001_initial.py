# Generated by Django 3.1.2 on 2020-11-30 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_posted', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]