from django.contrib import admin
from .models import *

#
# class DesktopAppAdmin(admin.ModelAdmin):
#     list_display = [field.name for field in Tbl_desktop_app._meta.fields]
#
#     # inlines = [ProductImageInline]
#     # list_filter = ('name',)
#     # search_fields = ['name']
#     # exclude = ('updated_by',)
#     readonly_fields = ('created', 'updated', 'updated_by',)
#     ordering = ('-index_number', '-id')
#
#     def save_model(self, request, obj, form, change):
#         # if not change:
#         obj.updated_by = request.user
#         obj.save()
#
#     class Meta:
#         model = Tbl_desktop_app
#
#
# admin.site.register(Tbl_desktop_app, DesktopAppAdmin)
#
#
# class MobileAppAdmin(admin.ModelAdmin):
#     list_display = [field.name for field in Tbl_mobile_app._meta.fields]
#
#     # inlines = [ProductImageInline]
#     # list_filter = ('name',)
#     # search_fields = ['name']
#     readonly_fields = ('created', 'updated', 'updated_by',)
#     ordering = ('-index_number', '-id')
#
#     def save_model(self, request, obj, form, change):
#         # if not change:
#         obj.updated_by = request.user
#         obj.save()
#
#     class Meta:
#         model = Tbl_mobile_app
#
#
# admin.site.register(Tbl_mobile_app, MobileAppAdmin)
#
#
# class InstructionsCapsAdmin(admin.ModelAdmin):
#     list_display = [field.name for field in Tbl_instructions_caps._meta.fields]
#
#     # inlines = [ProductImageInline]
#     # list_filter = ('name',)
#     # search_fields = ['name']
#     readonly_fields = ('created', 'updated', 'updated_by',)
#     ordering = ('-index_number', '-id')
#
#     def save_model(self, request, obj, form, change):
#         # if not change:
#         obj.updated_by = request.user
#         obj.save()
#
#     class Meta:
#         model = Tbl_instructions_caps
#
#
# admin.site.register(Tbl_instructions_caps, InstructionsCapsAdmin)
#
#
# class DownloadsAdmin(admin.ModelAdmin):
#     list_display = [field.name for field in Tbl_downloads._meta.fields]
#
#     # inlines = [ProductImageInline]
#     # list_filter = ('name',)
#     # search_fields = ['name']
#     readonly_fields = ('created', 'updated', 'updated_by',)
#     ordering = ('-index_number', '-id')
#
#     def save_model(self, request, obj, form, change):
#         # if not change:
#         obj.updated_by = request.user
#         obj.save()
#
#     class Meta:
#         model = Tbl_downloads
#
#
# admin.site.register(Tbl_downloads, DownloadsAdmin)
#
#
# class ArticlesBeerAdmin(admin.ModelAdmin):
#     list_display = [field.name for field in Tbl_articles_beer._meta.fields]
#
#     # inlines = [ProductImageInline]
#     # list_filter = ('name',)
#     # search_fields = ['name']
#     # exclude = ('updated_by',)
#     readonly_fields = ('created', 'updated', 'updated_by',)
#     ordering = ('-index_number', '-id')
#
#     def save_model(self, request, obj, form, change):
#         # if not change:
#         obj.updated_by = request.user
#         obj.save()
#
#     class Meta:
#         model = Tbl_articles_beer
#
#
# admin.site.register(Tbl_articles_beer, ArticlesBeerAdmin)
#
#
# class RequestFormsAdmin(admin.ModelAdmin):
#     list_display = [field.name for field in Tbl_request_forms._meta.fields]
#
#     # inlines = [ProductImageInline]
#     # list_filter = ('name',)
#     # search_fields = ['name']
#     readonly_fields = ('created', 'updated', 'updated_by',)
#     ordering = ('-index_number', '-id')
#
#     def save_model(self, request, obj, form, change):
#         # if not change:
#         obj.updated_by = request.user
#         obj.save()
#
#     class Meta:
#         model = Tbl_request_forms
#
#
# admin.site.register(Tbl_request_forms, RequestFormsAdmin)
