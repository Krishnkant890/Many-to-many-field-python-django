# Generated by Django 4.1.5 on 2023-02-10 18:01

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_name', models.CharField(max_length=10)),
                ('movi_duration', models.IntegerField()),
                ('Song', models.ManyToManyField(to='myapp.song')),
                ('User', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]