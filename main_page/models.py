from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

#
# class Tbl_desktop_app(models.Model):
#     index_number = models.SmallIntegerField(blank=True, null=True, default=None, unique=True)
#     topic = models.CharField(max_length=50, blank=True, null=True, default=None)
#     description = models.TextField(max_length=255, blank=True, null=True, default=None)
#     image = models.ImageField(upload_to='main_page/img', blank=True, null=True)
#     # image_link = models.CharField(max_length=255, blank=True, null=True,
#     #                               default='../static/main_page/img/')
#     link = models.URLField(max_length=250, blank=True, null=True, default=None)
#     is_active = models.BooleanField(default='True')
#     created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
#     updated = models.DateTimeField(auto_now=True, blank=True, null=True)
#     updated_by = models.ForeignKey(User, editable=True, on_delete=models.DO_NOTHING)
#
#     def __str__(self):
#         # return self.region_name + ' - ' + self.cust_name
#         return self.topic
#
#     class Meta:
#         verbose_name = 'desktop app'
#         verbose_name_plural = 'desktop apps'
#
#
# class Tbl_mobile_app(models.Model):
#     index_number = models.SmallIntegerField(blank=True, null=True, default=None, unique=True)
#     topic = models.CharField(max_length=50, blank=True, null=True, default=None)
#     description = models.TextField(max_length=255, blank=True, null=True, default=None)
#     image = models.ImageField(upload_to='main_page/img', blank=True, null=True)
#     # image_link = models.CharField(max_length=255, blank=True, null=True, default='../static/main_page/img/')
#     link = models.URLField(max_length=250, blank=True, null=True, default=None)
#     is_active = models.BooleanField(default='True')
#     created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
#     updated = models.DateTimeField(auto_now=True, blank=True, null=True, editable=True)
#     updated_by = models.ForeignKey(User, editable=True, on_delete=models.DO_NOTHING)
#
#     def __str__(self):
#         # return self.region_name + ' - ' + self.cust_name
#         return self.topic
#
#     class Meta:
#         verbose_name = 'mobile app'
#         verbose_name_plural = 'mobile apps'
#
#
# class Tbl_instructions_caps(models.Model):
#     index_number = models.SmallIntegerField(blank=True, null=True, default=None, unique=True)
#     topic = models.CharField(max_length=50, blank=True, null=True, default=None)
#     description = models.TextField(max_length=255, blank=True, null=True, default=None)
#     image = models.ImageField(upload_to='main_page/img', blank=True, null=True)
#     # image_link = models.CharField(max_length=255, blank=True, null=True,
#     #                               default='../static/main_page/img/')
#     link = models.URLField(max_length=250, blank=True, null=True, default=None)
#     is_active = models.BooleanField(default='True')
#     created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
#     updated = models.DateTimeField(auto_now=True, blank=True, null=True)
#     updated_by = models.ForeignKey(User, editable=True, on_delete=models.DO_NOTHING)
#
#     def __str__(self):
#         # return self.region_name + ' - ' + self.cust_name
#         return self.topic
#
#     class Meta:
#         verbose_name = 'Caps instruction'
#         verbose_name_plural = 'Caps instructions'
#
#
# class Tbl_downloads(models.Model):
#     index_number = models.SmallIntegerField(blank=True, null=True, default=None, unique=True)
#     topic = models.CharField(max_length=50, blank=True, null=True, default=None)
#     version = models.CharField(max_length=50, blank=True, null=True, default=None)
#     link = models.URLField(max_length=250, blank=True, null=True, default=None)
#     file = models.FileField(upload_to='main_page/file', blank=True, null=True)
#     is_active = models.BooleanField(default='True')
#     created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
#     updated = models.DateTimeField(auto_now=True, blank=True, null=True)
#     updated_by = models.ForeignKey(User, editable=True, on_delete=models.DO_NOTHING)
#
#     def __str__(self):
#         return self.topic + ' - ' + self.version
#         # return self.topic
#
#     class Meta:
#         verbose_name = 'Download'
#         verbose_name_plural = 'Downloads'
#
#
# class Tbl_articles_beer(models.Model):
#     index_number = models.SmallIntegerField(blank=True, null=True, default=None, unique=True)
#     topic = models.CharField(max_length=50, blank=True, null=True, default=None)
#     description = models.TextField(max_length=255, blank=True, null=True, default=None)
#     is_active = models.BooleanField(default='True')
#     created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
#     updated = models.DateTimeField(auto_now=True, blank=True, null=True)
#     updated_by = models.ForeignKey(User, editable=True, on_delete=models.DO_NOTHING)
#
#     def __str__(self):
#         return self.topic
#
#     class Meta:
#         verbose_name = 'Article about beer'
#         verbose_name_plural = 'Articles about beer'
#
#
# class Tbl_request_forms(models.Model):
#     index_number = models.SmallIntegerField(blank=True, null=True, default=None, unique=True)
#     topic = models.CharField(max_length=50, blank=True, null=True, default=None)
#     description = models.TextField(max_length=255, blank=True, null=True, default=None)
#     image = models.ImageField(upload_to='main_page/img', blank=True, null=True)
#     # image_link = models.CharField(max_length=255, blank=True, null=True,
#     #                               default='../static/main_page/img/')
#     link = models.URLField(max_length=250, blank=True, null=True, default=None)
#     is_active = models.BooleanField(default='True')
#     created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
#     updated = models.DateTimeField(auto_now=True, blank=True, null=True)
#     updated_by = models.ForeignKey(User, editable=True, on_delete=models.DO_NOTHING)
#
#     def __str__(self):
#         # return self.region_name + ' - ' + self.cust_name
#         return self.topic
#
#     class Meta:
#         verbose_name = 'request form'
#         verbose_name_plural = 'request forms'
