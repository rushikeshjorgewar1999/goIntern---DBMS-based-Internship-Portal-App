# Generated by Django 4.0.5 on 2022-06-23 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('pid', models.AutoField(primary_key=True, serialize=False)),
                ('pname', models.CharField(max_length=200)),
                ('pimg', models.ImageField(upload_to='')),
                ('price', models.IntegerField()),
                ('desc', models.TextField()),
                ('color', models.CharField(max_length=100)),
            ],
        ),
    ]
