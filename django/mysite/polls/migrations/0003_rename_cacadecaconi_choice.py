# Generated by Django 4.0.3 on 2022-04-09 00:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_rename_choice_cacadecaconi'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CacaDeCaconi',
            new_name='Choice',
        ),
    ]