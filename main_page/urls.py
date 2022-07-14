# from django.conf.urls import url, include
from main_page import views
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path

# Add a URL to urlpatterns:  path('', Home.as_view(), name='home')

urlpatterns = [
    path("", views.index_view, name='hoindexme')
    # url(r'^$', views.index_view, name='index'),
    # url(r'^request_form/(?P<pk>[0-9]+)', views.request_form_view, name='request_form'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
