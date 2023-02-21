from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Inventory, InventoryProgress


# class StaffAdmin(admin.ModelAdmin):
#     list_display = ('m4', 'm3', 'm2', 'Сектор', 'Name', 'Level',)
#     readonly_fields = ['m4', 'm3', 'm2', 'Сектор', 'Name', 'Level', 'orgstructureid']


class InventoryAdmin(admin.ModelAdmin):
    """
    Настраиваем отображение инвенты
    Отображение картинки брал здесь https://dvmn.org/encyclopedia/django/how-to-setup-image-preview/
    """
    list_display = ('id', 'user_id', 'org', 'model', 'sn', 'imei1', 'imei2', 'check_info', 'dlm')
    list_filter = ('check_info', 'dlm')
    search_fields = ['user_id', 'id', 'sn', 'imei1', 'imei2']
    date_hierarchy = 'dlm'
    readonly_fields = ['user_id', 'model', "preview", 'org']
    fields = ['model', 'sn', 'imei1', 'imei2', 'check_info', 'file_name', 'preview']
    list_select_related = ['org', ]  # для ускорения загрузки таблицы https://habr.com/ru/post/322114/
    ordering = ['-dlm']

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.file_name.url}" style="max-height: 700px;">')


class InventoryProgressAdmin(admin.ModelAdmin):
    """
    Настраиваем отображение инвенты по всему персоналу
    Отображение картинки брал здесь https://dvmn.org/encyclopedia/django/how-to-setup-image-preview/
    """
    list_display = ('m4', 'm3', 'm2', 'sector', 'Name', 'Level', 'type', 'model', 'check_info', 'dlm')
    list_filter = ('check_info', 'dlm', 'm4', 'Level', 'type')
    search_fields = ('m4', 'm3', 'm2', 'Name',)
    date_hierarchy = 'dlm'
    # readonly_fields = ['m4', 'm3', 'm2', 'sector', 'Name', 'Level', 'type', 'model', 'check_info', 'dlm' "preview"]
    fields = ['m4', 'm3', 'm2', 'sector', 'Name', 'Level', 'type', 'model', 'check_info', 'dlm', 'preview']
    # list_select_related = ['org', ]  # для ускорения загрузки таблицы https://habr.com/ru/post/322114/
    ordering = ['m4', 'm3', 'm2', 'sector', 'Name', ]

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.file_name.url}" style="max-height: 700px;">')


admin.site.register(Inventory, InventoryAdmin)
admin.site.register(InventoryProgress, InventoryProgressAdmin)
