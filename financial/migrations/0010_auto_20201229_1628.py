# Generated by Django 3.1.2 on 2020-12-29 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financial', '0009_auto_20201229_1613'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='payment',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='status',
            field=models.ManyToManyField(to='financial.Status'),
        ),
    ]