# Generated by Django 3.0.8 on 2020-08-07 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(default=0)),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=65)),
            ],
        ),
    ]
