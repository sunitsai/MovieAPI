# Generated by Django 3.1.6 on 2021-02-19 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('released', models.DateField(null=True)),
                ('rated', models.CharField(max_length=50)),
                ('genre', models.CharField(max_length=200)),
                ('imdbid', models.CharField(max_length=50)),
            ],
        ),
    ]
