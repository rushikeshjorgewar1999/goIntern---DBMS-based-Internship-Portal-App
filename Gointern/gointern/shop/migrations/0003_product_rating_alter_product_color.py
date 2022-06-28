# Generated by Django 4.0.5 on 2022-06-23 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_product_paperback'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='rating',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='color',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
