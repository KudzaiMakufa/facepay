# Generated by Django 3.0.8 on 2020-08-14 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=65),
        ),
    ]
