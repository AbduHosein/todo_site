# Generated by Django 4.0.7 on 2023-03-20 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_application_coverl_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='coverl_desc',
            field=models.CharField(default='test', max_length=200),
        ),
        migrations.AlterField(
            model_name='application',
            name='prev_desc',
            field=models.CharField(default='test', max_length=40),
        ),
    ]
