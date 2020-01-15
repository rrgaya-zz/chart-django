# Generated by Django 3.0.2 on 2020-01-15 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('sex', models.CharField(max_length=10)),
                ('survived', models.BooleanField()),
                ('age', models.FloatField()),
                ('ticket_class', models.PositiveSmallIntegerField()),
                ('embarked', models.CharField(max_length=3)),
            ],
            options={
                'verbose_name': 'Passenger',
                'verbose_name_plural': 'Passengers',
            },
        ),
    ]