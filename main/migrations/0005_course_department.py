# Generated by Django 4.0.7 on 2023-03-31 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_application_resume'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='department',
            field=models.CharField(default=0, max_length=4),
            preserve_default=False,
        ),
    ]
