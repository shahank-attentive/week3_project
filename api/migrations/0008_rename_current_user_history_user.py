# Generated by Django 3.2.17 on 2023-02-27 10:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_remove_history_model'),
    ]

    operations = [
        migrations.RenameField(
            model_name='history',
            old_name='current_user',
            new_name='user',
        ),
    ]
