# Generated by Django 2.1.2 on 2020-03-03 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board_main', '0007_auto_20200303_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardlist',
            name='date',
            field=models.DateTimeField(auto_now=True, db_column='DATE', null=True),
        ),
    ]
