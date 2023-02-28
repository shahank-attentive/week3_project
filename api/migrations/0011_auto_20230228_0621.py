# Generated by Django 3.2.17 on 2023-02-28 06:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20230228_0619'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicaldevice',
            name='current_user',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='api.employee'),
        ),
        migrations.RemoveField(
            model_name='device',
            name='current_user',
        ),
        migrations.AddField(
            model_name='device',
            name='current_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.employee'),
        ),
    ]