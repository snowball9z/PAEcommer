# Generated by Django 3.1 on 2021-03-26 08:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20210326_1459'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='descriptiom',
            new_name='description',
        ),
    ]
