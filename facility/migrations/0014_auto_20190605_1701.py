# Generated by Django 2.0 on 2019-06-05 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facility', '0013_auto_20190605_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facility',
            name='buyer',
            field=models.CharField(max_length=100, verbose_name='购买人'),
        ),
    ]