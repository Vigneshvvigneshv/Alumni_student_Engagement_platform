# Generated by Django 3.2.4 on 2025-03-30 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Event_id', models.CharField(max_length=15)),
                ('Name', models.CharField(max_length=50)),
                ('Image', models.ImageField(upload_to='')),
                ('Location', models.CharField(max_length=15)),
                ('Date', models.DateField()),
                ('Time', models.TimeField()),
                ('time_posted', models.DateTimeField(auto_now=True)),
                ('Description', models.CharField(max_length=400)),
            ],
        ),
    ]
