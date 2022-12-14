# Generated by Django 4.1 on 2022-08-22 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0005_alter_testmodel_options_testmodel_detailed_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='testmodel',
            options={'ordering': ('-created_at',), 'verbose_name_plural': 'Test Model'},
        ),
        migrations.CreateModel(
            name='ModelX',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mileage', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('test_content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='test_content', to='test_app.testmodel')),
            ],
            options={
                'verbose_name_plural': 'ModelX',
                'ordering': ('-created_at',),
            },
        ),
    ]
