# Generated by Django 3.1.2 on 2020-10-19 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_code', models.CharField(max_length=120)),
                ('response_time', models.CharField(max_length=120)),
                ('run_timedate', models.CharField(max_length=120)),
            ],
        ),
    ]
