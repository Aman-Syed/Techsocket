# Generated by Django 2.1 on 2022-08-01 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('techsocket', '0005_heyy'),
    ]

    operations = [
        migrations.CreateModel(
            name='Birthdays',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birth_day', models.CharField(max_length=5)),
                ('birth_month', models.CharField(max_length=20)),
                ('user_id', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Dm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rec_user_id', models.CharField(max_length=8)),
                ('send_user_id', models.CharField(max_length=8)),
                ('messages', models.TextField()),
                ('date', models.TextField()),
                ('time', models.TextField()),
                ('documents', models.TextField()),
                ('photos', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='EthicalValues',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ethical_value_name', models.TextField()),
                ('ethical_value_id', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rec_user_id', models.CharField(max_length=8)),
                ('send_user_id', models.CharField(max_length=8)),
                ('feedback_content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Greetings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('greeting_id', models.IntegerField()),
                ('greeting_name', models.TextField()),
                ('posted_date', models.TextField()),
                ('reactions', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Nominations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=8)),
                ('award_name', models.TextField()),
                ('no_of_nominations', models.IntegerField()),
                ('start_date', models.TextField()),
                ('end_date', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification_id', models.IntegerField()),
                ('notification_message', models.TextField()),
                ('user_id', models.CharField(max_length=8)),
                ('truth_value', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PersonalGoals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=8)),
                ('goal', models.TextField()),
                ('deadline', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PostReactions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=8)),
                ('reaction', models.TextField()),
                ('post_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PostReplies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.IntegerField()),
                ('user_id', models.CharField(max_length=8)),
                ('reply', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=8)),
                ('post', models.TextField()),
                ('post_id', models.IntegerField()),
                ('mentions', models.TextField()),
                ('given_coins', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='PostSeen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=30)),
                ('seen', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('query_id', models.IntegerField()),
                ('query', models.TextField()),
                ('hastags', models.TextField()),
                ('user_id', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='QueryReplies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('query_id', models.IntegerField()),
                ('reply', models.TextField()),
                ('user_id', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='SkillList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_id', models.CharField(max_length=10)),
                ('skill_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.TextField()),
                ('team_id', models.IntegerField()),
                ('user_id', models.CharField(max_length=8)),
                ('members_list', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TeamGoals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_id', models.IntegerField()),
                ('goal', models.TextField()),
                ('deadline', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=8)),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.TextField()),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('user_id', models.CharField(max_length=8)),
                ('address', models.TextField()),
                ('phone_no', models.CharField(max_length=13)),
                ('educational_qualifications', models.TextField()),
                ('designation', models.CharField(max_length=50)),
                ('join_date', models.CharField(max_length=20)),
                ('join_year', models.TextField(default=0)),
                ('join_month', models.TextField(default=0)),
                ('join_date_no', models.TextField(default=0)),
                ('social_media', models.TextField(default=0)),
                ('techie_coins', models.IntegerField(default=100)),
                ('skills', models.TextField(default=10)),
            ],
        ),
        migrations.DeleteModel(
            name='Heyy',
        ),
    ]
