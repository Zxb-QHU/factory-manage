# Generated by Django 2.0 on 2019-06-02 03:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0014_auto_20190602_1153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='staff_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='user.Position', verbose_name='职位'),
        ),
    ]
