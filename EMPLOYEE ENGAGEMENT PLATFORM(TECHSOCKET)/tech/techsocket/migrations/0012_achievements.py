# Generated by Django 2.1 on 2022-08-01 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('techsocket', '0011_auto_20220801_1137'),
    ]

    operations = [
        migrations.CreateModel(
            name='Achievements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('achievement_id', models.IntegerField()),
                ('achievement_name', models.TextField()),
                ('user_id', models.CharField(max_length=8)),
                ('month', models.TextField()),
                ('year', models.TextField()),
            ],
        ),
    ]
