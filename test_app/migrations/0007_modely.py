# Generated by Django 4.1 on 2022-08-22 12:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0006_alter_testmodel_options_modelx'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelY',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mileage', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('test_cont', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='test_cont', to='test_app.testmodel')),
            ],
            options={
                'verbose_name_plural': 'ModelY',
                'ordering': ('-created_at',),
            },
        ),
    ]