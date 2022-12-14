# Generated by Django 4.0.6 on 2022-07-29 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=40)),
                ('age', models.FloatField()),
                ('genre', models.CharField(max_length=40)),
                ('relative', models.CharField(max_length=40)),
                ('creation_date', models.DateField(auto_now_add=True, null=True)),
            ],
        ),
    ]
