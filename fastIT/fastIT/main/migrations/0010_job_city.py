# Generated by Django 3.1.5 on 2021-01-08 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20210108_1913'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='city',
            field=models.TextField(blank=True, max_length=30),
        ),
    ]
