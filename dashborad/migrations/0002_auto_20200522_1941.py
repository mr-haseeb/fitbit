# Generated by Django 3.0.6 on 2020-05-22 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashborad', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='steps',
            field=models.DecimalField(decimal_places=6, max_digits=10),
        ),
    ]
