# Generated by Django 2.1 on 2022-08-02 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('techsocket', '0013_notifications_notification'),
    ]

    operations = [
        migrations.CreateModel(
            name='Incentives',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('incentive_id', models.IntegerField()),
                ('incentive', models.TextField()),
                ('techie_coins', models.IntegerField()),
            ],
        ),
    ]
