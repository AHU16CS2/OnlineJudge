# Generated by Django 2.1.1 on 2018-10-13 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oj_base', '0002_auto_20181013_1202'),
    ]

    operations = [
        migrations.CreateModel(
            name='motto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=30)),
                ('content', models.TextField()),
            ],
        ),
    ]
