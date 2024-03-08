# Generated by Django 4.0.4 on 2024-03-08 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BrokerQuery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('broker', models.CharField(max_length=50)),
                ('parameters', models.JSONField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('last_run', models.DateTimeField(blank=True, default=None, null=True)),
            ],
        ),
    ]
