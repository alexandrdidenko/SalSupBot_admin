# Generated by Django 4.0.6 on 2022-07-14 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0015_alter_users_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Chanel', models.CharField(blank=True, db_column='Тип деятельностьи', max_length=300, null=True)),
                ('Level', models.CharField(blank=True, max_length=50, null=True)),
                ('Name', models.CharField(blank=True, max_length=300, null=True)),
                ('Sector', models.CharField(blank=True, db_column='Сектор', max_length=300, null=True)),
                ('m2', models.CharField(blank=True, max_length=300, null=True)),
                ('m3', models.CharField(blank=True, max_length=300, null=True)),
                ('m4', models.CharField(blank=True, max_length=300, null=True)),
                ('orgstructureid', models.CharField(blank=True, max_length=37, null=True, unique=True)),
            ],
            options={
                'verbose_name': 'Персонал',
                'verbose_name_plural': 'Персонал',
                'db_table': '[bot].[view_staff]',
            },
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('src', models.ImageField(upload_to='')),
                ('model', models.CharField(blank=True, max_length=50, null=True)),
                ('shot', models.IntegerField(blank=True, null=True)),
                ('dlm', models.DateTimeField(blank=True, null=True)),
                ('sn', models.CharField(blank=True, max_length=50, null=True)),
                ('imei2', models.CharField(blank=True, max_length=50, null=True)),
                ('check_info', models.BooleanField(blank=True, null=True)),
                ('imei1', models.CharField(blank=True, max_length=50, null=True)),
                ('user_id', models.BigIntegerField(unique=True)),
                ('org', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='bot.staff', to_field='orgstructureid')),
            ],
            options={
                'verbose_name': 'Инвентаризация',
                'verbose_name_plural': 'Инвентаризация',
                'db_table': '[bot].[inventory_test]',
            },
        ),
    ]
