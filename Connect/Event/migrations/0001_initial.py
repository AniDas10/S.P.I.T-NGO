# Generated by Django 3.0.2 on 2020-02-01 16:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('NGO', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('date_of_event', models.DateTimeField()),
                ('published', models.DateTimeField(auto_now_add=True)),
                ('purpose', models.TextField()),
                ('rsvp', models.IntegerField(default=0)),
                ('event_poster', models.ImageField(upload_to='Events/Posters')),
                ('tagline', models.CharField(max_length=540)),
                ('sentiment', models.IntegerField(default=0)),
                ('expected_footfall', models.BigIntegerField()),
                ('price', models.IntegerField(default=0)),
                ('location', models.TextField()),
                ('ngo', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='NGO.NGO')),
            ],
        ),
    ]
