# Generated by Django 3.2.25 on 2024-11-01 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0105_delete_invalid_attempts'),
    ]

    operations = [
        migrations.RenameField(
            model_name='episode',
            old_name='r_blocklyEnabled',
            new_name='r_blockly_enabled',
        ),
        migrations.RenameField(
            model_name='episode',
            old_name='r_pythonEnabled',
            new_name='r_python_enabled',
        ),
        migrations.RenameField(
            model_name='episode',
            old_name='r_trafficLights',
            new_name='r_traffic_lights',
        ),
        migrations.RenameField(
            model_name='level',
            old_name='blocklyEnabled',
            new_name='blockly_enabled',
        ),
        migrations.RenameField(
            model_name='level',
            old_name='pythonEnabled',
            new_name='python_enabled',
        ),
        migrations.RenameField(
            model_name='level',
            old_name='pythonViewEnabled',
            new_name='python_view_enabled',
        ),
        migrations.RenameField(
            model_name='leveldecor',
            old_name='decorName',
            new_name='decor_name',
        ),
    ]