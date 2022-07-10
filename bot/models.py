from django.db import models
from django.utils import timezone


class Roles(models.Model):
    """Модель ролей"""
    role_name = models.CharField(max_length=20)

    class Meta:
        db_table = "[bot].[bot_roles]"
        verbose_name = 'Роль'
        verbose_name_plural = 'Роли'

    def publish(self):
        self.save()

    def __str__(self):
        return self.role_name


class Groups(models.Model):
    """Модель групп пользователей"""
    group_name = models.CharField(max_length=10)
    link_roles = models.ManyToManyField(to=Roles, db_table="[bot].[bot_group_in_roles]", blank=True)

    class Meta:
        db_table = "[bot].[bot_groups]"
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

    def display_roles(self):
        """Выводим поля с привязками ManyToMany в один столбец"""
        return ', '.join([link_roles.role_name for link_roles in self.link_roles.all()])

    link_roles.short_description = 'Роли'

    def publish(self):
        self.save()

    def __str__(self):
        return self.group_name


class Users(models.Model):
    """Модель пользователей"""
    user_id = models.BigIntegerField(null=False, unique=True)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    username = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    org_name = models.CharField(max_length=100, null=True, blank=True)
    org_id = models.CharField(max_length=37, null=True, blank=True)
    org_email = models.EmailField(default=None, null=True, blank=True)
    link_groups = models.ManyToManyField(to=Groups, db_table="[bot].[bot_user_in_groups]", blank=True)
    created = models.DateTimeField(default=timezone.now, null=True, blank=True)
    updated = models.DateTimeField(null=False, auto_now=True)
    deleted = models.DateTimeField(blank=True, null=True)
    last_visit = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = "[bot].[bot_users]"
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def display_groups(self):
        """Выводим поля с привязками ManyToMany в один столбец"""
        return ', '.join([link_groups.group_name for link_groups in self.link_groups.all()])

    link_groups.short_description = 'Группы'

    def publish(self):
        self.updated = timezone.now()
        self.save()

    def __str__(self):
        return str(self.last_name) + ' ' + str(self.first_name)
