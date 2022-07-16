from inventory import views
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('inventory_list/', views.inventory_list_view, name='inventory_list'),
    path('info_about_tablet/<str:pk>', views.info_about_tablet_view, name='info_about_tablet'),
    path('info_about_tablet/<str:pk>/edit', views.edit_tablet_view, name='edit_tablet'),

    # path('', include(('home.urls', 'home'), namespace='home'))


    # url(r'^info_about_tablet/(?P<pk>[0-9]+)/edit$', views.edit_tablet_view, name='edit_tablet'),
    # url(r'^info_about_tablet/(?P<pk>[0-9]+)/delete$', views.delete_tablet_view, name='delete_tablet'),
    # url(r'^info_about_tablet/(?P<pk>[0-9]+)/$', views.info_about_tablet_view, name='info_about_tablet'),
    # url(r'^add_new_tablet/$', views.add_new_tablet_view, name='add_new_tablet'),
    # # url(r'^all_tablets/export/csv/$', views.export_to_csv_all_tablets_view, name='export_to_csv_all_tablets_view'),
    # url(r'^all_tablets/export/excel/$', views.export_to_excel_all_tablets_view,
    #     name='export_to_excel_all_tablets_view'),
]
