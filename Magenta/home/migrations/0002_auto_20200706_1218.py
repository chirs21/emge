# Generated by Django 3.0.7 on 2020-07-06 12:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='selfie',
            new_name='ph1',
        ),
    ]