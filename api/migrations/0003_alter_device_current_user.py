# Generated by Django 3.2.17 on 2023-02-17 08:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20230217_0710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='current_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.employee'),
        ),
    ]
