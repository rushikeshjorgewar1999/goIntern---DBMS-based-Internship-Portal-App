# Generated by Django 4.0.5 on 2022-06-21 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_remove_company_register_company_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company_register',
            old_name='conpassword',
            new_name='username',
        ),
    ]
