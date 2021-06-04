# Generated by Django 3.1.7 on 2021-05-07 10:34

import backend.classes.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0003_auto_20210505_2312'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invites',
            fields=[
                ('id', models.CharField(default=backend.classes.models.uuid64bit, editable=False, max_length=8, primary_key=True, serialize=False, unique=True)),
                ('classes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='classes', to='classes.classes')),
            ],
        ),
    ]