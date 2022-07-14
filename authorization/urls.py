# from django.conf.urls import url, include
from authorization import views
from django.urls import path
urlpatterns = [
    path(r'logon/', views.logon_view, name='logon'),
    path(r'logout/', views.logout_view, name='logout'),

]
