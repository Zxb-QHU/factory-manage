# Generated by Django 2.0 on 2019-06-09 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0023_auto_20190609_2343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='staff_type',
            field=models.CharField(max_length=100, null=True, verbose_name='职位'),
        ),
    ]