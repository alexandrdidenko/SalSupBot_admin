# -*- coding: utf-8 -*-
from django.contrib import auth
from django.shortcuts import render, redirect, HttpResponse
from main_page.models import *


# Create your views here.
def index_view(request):
    username = auth.get_user(request)
    # username_sesion = auth._get_user_session_key(request)
    # all_desktop_app = Tbl_desktop_app.objects.raw(
    #     '''select * from main_page_tbl_desktop_app WHERE is_active = TRUE order by index_number''')
    # all_mobile_app = Tbl_mobile_app.objects.raw(
    #     '''select * from main_page_tbl_mobile_app WHERE is_active = TRUE order by index_number''')
    # all_instructions_caps = Tbl_instructions_caps.objects.raw(
    #     '''select * from main_page_tbl_instructions_caps WHERE is_active = TRUE order by index_number''')
    # all_downloads = Tbl_downloads.objects.raw(
    #     '''select * from main_page_tbl_downloads WHERE is_active = TRUE order by index_number''')
    # articles_beer_1 = Tbl_articles_beer.objects.raw(
    #     '''select * from main_page_tbl_articles_beer WHERE is_active = TRUE and index_number = 1''')
    # articles_beer_2 = Tbl_articles_beer.objects.raw(
    #     '''select * from main_page_tbl_articles_beer WHERE is_active = TRUE and index_number = 2''')
    # articles_beer_3 = Tbl_articles_beer.objects.raw(
    #     '''select * from main_page_tbl_articles_beer WHERE is_active = TRUE and index_number = 3''')
    # articles_beer_4 = Tbl_articles_beer.objects.raw(
    #     '''select * from main_page_tbl_articles_beer WHERE is_active = TRUE and index_number = 4''')
    # articles_beer_5 = Tbl_articles_beer.objects.raw(
    #     '''select * from main_page_tbl_articles_beer WHERE is_active = TRUE and index_number = 5''')
    # all_form = Tbl_request_forms.objects.raw(
    #     '''select * from main_page_tbl_request_forms WHERE is_active = TRUE and index_number >= 1''')
    arg = {
        'username': username,
        # 'all_desktop_app': all_desktop_app,
        # 'all_mobile_app': all_mobile_app,
        # 'all_instructions_caps': all_instructions_caps,
        # 'all_downloads': all_downloads,
        # 'articles_beer_1': articles_beer_1,
        # 'articles_beer_2': articles_beer_2,
        # 'articles_beer_3': articles_beer_3,
        # 'articles_beer_4': articles_beer_4,
        # 'articles_beer_5': articles_beer_5,
        # 'all_form': all_form,
    }
    if username.is_anonymous:
        username = ''
        # return redirect('/logon')
        # return render(request, 'main_page/index.html', locals())
        return render(request, 'main_page/index.html', locals())
    else:
        # return render(request, 'main_page/index.html', {'username': username})
        return render(request, 'main_page/index.html', arg)

#
# def request_form_view(request, pk):
#     username = auth.get_user(request)
#     selected_form = Tbl_request_forms.objects.raw(
#         '''select * from main_page_tbl_request_forms WHERE is_active = TRUE and index_number = %s''' % pk)
#     arg = {
#         'username': username,
#         'selected_form': selected_form,
#     }
#     if username.is_anonymous:
#         username = ''
#         return render(request, 'request_forms/request_form.html', locals())
#     else:
#         return render(request, 'request_forms/request_form.html', arg)
