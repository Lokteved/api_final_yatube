# Generated by Django 3.1 on 2020-08-31 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20200831_1820'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='pub_date',
            new_name='created',
        ),
    ]
