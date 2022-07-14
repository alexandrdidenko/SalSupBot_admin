from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Users, Groups, Roles, Inventory, Staff


class UsersAdmin(admin.ModelAdmin):
    """Настраиваем отображение в админке пользователей"""
    list_display = (
        'id', 'user_id', 'first_name', 'last_name', 'phone', 'org_name',
        'last_visit')  # если нужно смотреть группы, 'display_groups'
    list_filter = ('last_visit', 'link_groups')
    search_fields = ('first_name', 'last_name', 'phone', 'org_name')
    prepopulated_fields = {'first_name': ('last_name',)}
    # raw_id_fields = ('id',)
    date_hierarchy = 'created'
    ordering = ['-id']  # сортировка в обратном порядке добавить -

    def get_readonly_fields(self, request, obj=None):
        """Запрещаем редактировать определенные поля"""
        if obj:  # when editing an object
            return ['user_id', 'phone', 'org_name', 'org_id', 'org_email', 'created', 'deleted', 'last_visit']
        return self.readonly_fields


class GroupsAdmin(admin.ModelAdmin):
    """Настраиваем отображение в админке групп пользователей"""
    list_display = ('id', 'group_name', 'display_roles')
    list_filter = ('link_roles',)
    search_fields = ('group_name',)
    # prepopulated_fields = {'first_name': ('last_name',)}
    # raw_id_fields = ('id',)
    ordering = ['id']  # сортировка в обратном порядке добавить -


class RolesAdmin(admin.ModelAdmin):
    """Настраиваем отображение в ролей для групп"""
    list_display = ('id', 'role_name')
    list_filter = ('role_name',)
    search_fields = ('role_name',)
    # prepopulated_fields = {'first_name': ('last_name',)}
    # raw_id_fields = ('id',)
    ordering = ['id']  # сортировка в обратном порядке добавить -


# class StaffAdmin(admin.ModelAdmin):
#     list_display = ('m4', 'm3', 'm2', 'Сектор', 'Name', 'Level',)
#     readonly_fields = ['m4', 'm3', 'm2', 'Сектор', 'Name', 'Level', 'orgstructureid']


class InventoryAdmin(admin.ModelAdmin):
    """
    Настраиваем отображение инвенты
    Отображение картинки брал здесь https://dvmn.org/encyclopedia/django/how-to-setup-image-preview/
    """
    list_display = ( 'user_id', 'org', 'model', 'sn', 'imei1', 'imei2', 'check_info', 'src','dlm')
    list_filter = ('check_info', 'dlm')
    search_fields = ('org',)
    readonly_fields = ['user_id', 'model', "preview", 'org']
    fields = ['user_id', 'model', 'sn', 'imei1', 'imei2', 'check_info', 'src', 'preview']
    list_select_related = ['org', ] #
    ordering = ['-dlm']
    def preview(self, obj):
        return mark_safe(f'<img src="{obj.src.url}" style="max-height: 800px;">')


admin.site.register(Users, UsersAdmin)
admin.site.register(Groups, GroupsAdmin)
admin.site.register(Roles, RolesAdmin)
admin.site.register(Inventory, InventoryAdmin)
# admin.site.register(Staff, StaffAdmin)

# admin.site.register(Users)
