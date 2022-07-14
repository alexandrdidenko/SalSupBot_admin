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


class Staff(models.Model):
    """Моделмь персонала"""
    Chanel = models.CharField(db_column='Тип деятельностьи', max_length=300, null=True, blank=True)
    Level = models.CharField(max_length=50, null=True, blank=True)
    Name = models.CharField(max_length=300, null=True, blank=True)
    Sector = models.CharField(db_column='Сектор', max_length=300, null=True, blank=True)
    m2 = models.CharField(max_length=300, null=True, blank=True)
    m3 = models.CharField(max_length=300, null=True, blank=True)
    m4 = models.CharField(max_length=300, null=True, blank=True)
    orgstructureid = models.CharField(max_length=37, null=True, blank=True, unique=True)

    class Meta:
        db_table = "[bot].[view_staff]"
        verbose_name = 'Персонал'
        verbose_name_plural = 'Персонал'

    def publish(self):
        self.save()

    def __str__(self):
        return self.m4 + r' \ ' + self.m3 + r' \ ' + self.Name


class Inventory(models.Model):
    """Моделмь инвенты планшетов"""
    file_name = models.ImageField(height_field=None, width_field=None, max_length=100)
    model = models.CharField(max_length=50, null=True, blank=True)
    # org_id = models.CharField(max_length=50, null=True, blank=True)
    org = models.OneToOneField(to=Staff, to_field='orgstructureid', on_delete=models.DO_NOTHING, null=True, blank=True)
    shot = models.IntegerField(null=True, blank=True)
    dlm = models.DateTimeField(null=True, blank=True)
    sn = models.CharField(max_length=50, null=True, blank=True)
    imei2 = models.CharField(max_length=50, null=True, blank=True)
    check_info = models.BooleanField(null=True, blank=True)
    imei1 = models.CharField(max_length=50, null=True, blank=True)
    user_id = models.BigIntegerField(null=False, unique=True)

    class Meta:
        db_table = "[bot].[bot_inventory]"
        verbose_name = 'Инвентаризация'
        verbose_name_plural = 'Инвентаризация'

    def publish(self):
        self.save()

    def __str__(self):
        return str(self.org)
