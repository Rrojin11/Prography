# Generated by Django 2.1.2 on 2020-03-02 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Boardlist',
            fields=[
                ('id', models.AutoField(db_column='NO', primary_key=True, serialize=False)),
                ('pcode', models.CharField(db_column='PCODE', max_length=4)),
                ('user_id', models.CharField(blank=True, db_column='USER_ID', max_length=50, null=True)),
                ('title', models.CharField(db_column='TITLE', max_length=100)),
                ('content', models.CharField(blank=True, db_column='CONTENT', max_length=1000, null=True)),
                ('priority', models.IntegerField(blank=True, db_column='PRIORITY', null=True)),
                ('date', models.DateField(blank=True, db_column='DATE', null=True)),
            ],
        ),
    ]
