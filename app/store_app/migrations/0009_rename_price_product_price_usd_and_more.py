# Generated by Django 4.0.4 on 2022-06-03 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0008_rename_name_currency_character_currency_cur_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='price',
            new_name='price_USD',
        ),
        migrations.RemoveField(
            model_name='product',
            name='currency',
        ),
    ]
