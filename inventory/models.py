from django.db import models
from django.utils import timezone


# Create your models here.


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


class InventoryProgress(models.Model):
    """Моделмь инвенты планшетов весь персонал"""

    m4 = models.CharField(max_length=300, null=True, blank=True)
    m3 = models.CharField(max_length=300, null=True, blank=True)
    m2 = models.CharField(max_length=300, null=True, blank=True)
    sector = models.CharField(max_length=300, null=True, blank=True)
    Name = models.CharField(max_length=300, null=True, blank=True)
    Level = models.CharField(max_length=6, null=True, blank=True)
    type = models.CharField(max_length=50, null=True, blank=True)
    model = models.CharField(max_length=50, null=True, blank=True)
    check_info = models.BooleanField(null=True, blank=True)
    dlm = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "[bot].[view_inventory_staff_progress]"
        verbose_name = 'Инвентаризация прогресс'
        verbose_name_plural = 'Инвентаризация прогресс (недоделанная !!!)'

    def publish(self):
        self.save()

    def __str__(self):
        return str(self.Name)
