# Generated by Django 3.1 on 2020-08-22 16:57

from django.db import migrations

import procrastinate.contrib.django


class Migration(migrations.Migration):

    dependencies = [
        ("procrastinate", "0007_add_queueing_lock_column"),
    ]

    operations = [
        procrastinate.contrib.django.RunProcrastinateFile(
            filename="delta_0.10.0_001_close_fetch_job_race_condition.sql",
        ),
    ]
