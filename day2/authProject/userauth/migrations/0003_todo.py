# Generated by Django 3.1.4 on 2020-12-21 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0002_auto_20201221_1408'),
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
