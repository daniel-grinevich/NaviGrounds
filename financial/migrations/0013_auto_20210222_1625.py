# Generated by Django 3.1.2 on 2021-02-22 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financial', '0012_auto_20210222_1517'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='type',
        ),
        migrations.AddField(
            model_name='payment',
            name='type',
            field=models.CharField(choices=[('Contribution', 'CONTRIBUTION'), ('Personal Expense', 'PERSONALEXPENSE'), ('Company Expense', 'COMPANYEXPENSE')], default='Contribution', max_length=22),
        ),
    ]