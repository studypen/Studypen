# Generated by Django 3.1.7 on 2021-04-02 05:07

import backend.classes.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=10)),
                ('id', models.CharField(default=backend.classes.models.uuid64bit, max_length=8, primary_key=True, serialize=False, unique=True)),
                ('students', models.ManyToManyField(related_name='class_students', to=settings.AUTH_USER_MODEL)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='classes_teacher', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SheduleTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_of_week', models.IntegerField(choices=[(1, 'Sunday'), (2, 'Monday'), (3, 'Tuseday'), (4, 'Wednesday'), (5, 'Thursday'), (6, 'Friday'), (7, 'Saturday')])),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('classes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classes.classes')),
            ],
        ),
        migrations.CreateModel(
            name='ResheduleTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('new_start_time', models.TimeField()),
                ('new_end_time', models.TimeField()),
                ('original_shedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classes.sheduletime')),
            ],
        ),
    ]
