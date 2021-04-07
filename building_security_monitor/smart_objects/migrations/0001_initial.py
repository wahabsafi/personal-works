# Generated by Django 3.1.7 on 2021-04-01 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_open', models.BooleanField(verbose_name='open status')),
                ('last_opened', models.TimeField(auto_now=True, verbose_name='last time opened')),
                ('password', models.CharField(max_length=50, verbose_name='lock password')),
            ],
            options={
                'verbose_name': 'Lock',
                'verbose_name_plural': 'Locks',
            },
        ),
    ]
