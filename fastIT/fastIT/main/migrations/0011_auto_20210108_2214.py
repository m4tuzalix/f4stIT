# Generated by Django 3.1.5 on 2021-01-08 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_job_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='position',
            field=models.TextField(max_length=50),
        ),
    ]
