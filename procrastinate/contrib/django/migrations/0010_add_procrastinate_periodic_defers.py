# Generated by Django 3.1 on 2020-08-22 16:57

from django.db import migrations

import procrastinate.contrib.django.utils


class Migration(migrations.Migration):

    dependencies = [
        ("procrastinate", "0009_add_defer_job_function"),
    ]

    operations = [
        procrastinate.contrib.django.utils.RunProcrastinateFile(
            filename="delta_0.11.0_003_add_procrastinate_periodic_defers.sql",
        ),
    ]
