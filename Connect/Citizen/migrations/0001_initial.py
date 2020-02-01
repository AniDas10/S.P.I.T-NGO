# Generated by Django 3.0.2 on 2020-02-01 16:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Event', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('NGO', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Citizen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField()),
                ('is_volunteer', models.BooleanField(default=False)),
                ('picture', models.ImageField(upload_to='Citizen/Photos')),
                ('date_of_joining', models.DateTimeField(auto_now_add=True)),
                ('points', models.IntegerField(default=10)),
                ('city', models.CharField(max_length=240)),
                ('email', models.EmailField(max_length=254)),
                ('events', models.ManyToManyField(to='Event.Event')),
                ('follows', models.ManyToManyField(to='NGO.NGO')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]