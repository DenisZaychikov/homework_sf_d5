# Generated by Django 2.2.6 on 2020-05-26 08:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0006_book_is_avaliable'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='is_avaliable',
            new_name='is_available',
        ),
    ]
