# Generated by Django 2.2 on 2022-12-05 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='basics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=225)),
                ('lastname', models.CharField(max_length=225)),
            ],
        ),
    ]
