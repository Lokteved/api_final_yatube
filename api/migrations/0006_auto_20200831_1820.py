# Generated by Django 3.1 on 2020-08-31 15:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20200831_1816'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='created',
            new_name='pub_date',
        ),
    ]
