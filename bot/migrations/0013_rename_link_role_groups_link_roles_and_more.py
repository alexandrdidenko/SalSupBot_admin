# Generated by Django 4.0.6 on 2022-07-10 14:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0012_rename_groups_groups_link_role'),
    ]

    operations = [
        migrations.RenameField(
            model_name='groups',
            old_name='link_role',
            new_name='link_roles',
        ),
        migrations.RenameField(
            model_name='users',
            old_name='groups',
            new_name='link_groups',
        ),
    ]
