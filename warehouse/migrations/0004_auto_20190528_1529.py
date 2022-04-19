# Generated by Django 2.0 on 2019-05-28 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0003_purchaselist'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProduceDiary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_time', models.DateField(auto_now_add=True, verbose_name='日期')),
                ('facility_id', models.IntegerField(default=0, verbose_name='设备')),
                ('staff_name', models.IntegerField(default=0, verbose_name='员工')),
                ('product_name', models.IntegerField(default=0, verbose_name='产品')),
                ('today_done_num', models.IntegerField(default=0, verbose_name='今日产量')),
                ('qualified_num', models.IntegerField(default=0, verbose_name='合格量')),
            ],
        ),
        migrations.AlterField(
            model_name='purchaselist',
            name='buyer_date',
            field=models.DateField(auto_now=True, verbose_name='采购日期'),
        ),
        migrations.AlterField(
            model_name='purchaselist',
            name='buyer_name',
            field=models.CharField(max_length=100, verbose_name='采购员'),
        ),
        migrations.AlterField(
            model_name='purchaselist',
            name='sanction_date',
            field=models.DateField(auto_now=True, verbose_name='批准日期'),
        ),
        migrations.AlterField(
            model_name='warehouse',
            name='current_time',
            field=models.DateField(auto_now_add=True, verbose_name='日期'),
        ),
    ]