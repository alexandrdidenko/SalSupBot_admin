# Generated by Django 4.0.6 on 2022-07-10 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0010_roles'),
    ]

    operations = [
        migrations.AddField(
            model_name='groups',
            name='groups',
            field=models.ManyToManyField(blank=True, db_table='[bot].[bot_group_in_roles]', to='bot.roles'),
        ),
    ]
