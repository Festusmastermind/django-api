# Generated by Django 4.1 on 2022-08-22 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='testmodel',
            old_name='is_live',
            new_name='is_alive',
        ),
    ]
