# Generated by Django 2.1 on 2022-08-06 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('techsocket', '0017_questions'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAnswers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic_id', models.IntegerField()),
                ('user_id', models.CharField(max_length=8)),
                ('score', models.IntegerField()),
            ],
        ),
    ]
