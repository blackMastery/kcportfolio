# Generated by Django 3.0.7 on 2020-07-02 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_intros'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='finish_date',
        ),
        migrations.RemoveField(
            model_name='project',
            name='start_date',
        ),
    ]
