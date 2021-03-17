# Generated by Django 3.1.7 on 2021-03-13 21:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('drf_accounts', '0003_account_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]