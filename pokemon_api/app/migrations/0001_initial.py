# Generated by Django 3.1.5 on 2021-01-18 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('pokemon_type', models.CharField(max_length=45)),
                ('ability', models.CharField(max_length=45)),
            ],
        ),
    ]
