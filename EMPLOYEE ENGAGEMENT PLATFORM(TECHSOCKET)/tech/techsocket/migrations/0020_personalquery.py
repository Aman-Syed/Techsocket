# Generated by Django 2.1 on 2022-08-06 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('techsocket', '0019_usernominate'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalQuery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pquery_type', models.TextField()),
                ('pquery_id', models.IntegerField()),
                ('pquery', models.TextField()),
                ('user_id', models.CharField(max_length=8)),
            ],
        ),
    ]