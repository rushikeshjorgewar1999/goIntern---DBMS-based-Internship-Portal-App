# Generated by Django 4.0.5 on 2022-06-23 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('internship', '0006_jobposting_benefits'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobposting',
            name='qualification',
            field=models.CharField(default='', max_length=1000),
        ),
    ]