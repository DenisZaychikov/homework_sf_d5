# Generated by Django 2.2.6 on 2020-05-25 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0004_auto_20200525_1436'),
    ]

    operations = [
        migrations.AddField(
            model_name='friend',
            name='full_name',
            field=models.TextField(default=None),
        ),
    ]
