# Generated by Django 2.1 on 2022-08-01 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('techsocket', '0009_auto_20220801_1004'),
    ]

    operations = [
        migrations.CreateModel(
            name='Awards',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('award_id', models.IntegerField()),
                ('winner_id', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Nominate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('award_id', models.IntegerField()),
                ('user_id', models.CharField(max_length=8)),
                ('no_of_nominations', models.IntegerField()),
            ],
        ),
    ]
