from django.shortcuts import render
# -*- coding: utf-8 -*-
from django.db import connection
from django.shortcuts import HttpResponse, redirect
from django.shortcuts import render, get_object_or_404
from django.contrib import auth
from django.utils import timezone

from inventory.models import *
from .forms import Tbl_tablet_list_Form

import csv
# import xlwt
import datetime

from django.http import HttpResponse, HttpResponseForbidden
from django.contrib.auth.models import User


def inventory_list_view(request):
    username = auth.get_user(request)

    if username.is_anonymous:
        username = ''
        return redirect('/logon')
    else:
        all_tablets = Inventory.objects.raw('''select s.file_name,
       RNK,
       id,
       user_id,
       dlm,
       case
           when check_info = 1 then 'Ok'
           when check_info = 0 then 'Not ok!'
           else '' end as [check_info],
        IIF(imei2 is null, '', imei2) as [imei2],
       IIF(imei1 is null, '', imei1) as [imei1],
       IIF(sn is null, '', sn) as [sn],
       model,
       type,
       Level,
       Name,
       sector,
       m2,
       m3,
       m4
from [bot].[view_inventory_staff] s
order by dlm DESC''')
        arg = {
            'username': username,
            'all_tablets': all_tablets,
        }
        return render(request, 'inventory/inventory_list.html', arg)


def info_about_tablet_view(request, pk):
    # not_in_tablets = Tbl_tablets_list.objects.raw('''call pda_sp_not_in_tablets_list()''')

    username = auth.get_user(request)
    # print(username.pk)

    if username.is_anonymous:
        username = ''
        return redirect('/logon')
    else:
        tablet = get_object_or_404(Inventory, pk=pk)
        history = Inventory.objects.raw(
            '''SELECT * FROM bot.bot_inventory where id = ('%s') order by id  DESC''' % pk)
        arg = {
            'username': username,
            'tablet': tablet,
            'history': history,

        }

        return render(request, 'inventory/info_about_tablet.html', arg)


def edit_tablet_view(request, pk):
    username = auth.get_user(request)
    username_id = auth.get_user(request).pk

    def my_custom_sql(query):
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        connection.close()
        return result

    sql = '''SELECT file_name FROM bot.bot_inventory where id = {pk}'''.format(pk=pk)
    my_file = my_custom_sql(sql)

    if username.is_anonymous:
        username = ''
        return redirect('/logon')
    else:
        post = get_object_or_404(Inventory, pk=pk)
        if request.method == "POST":
            form = Tbl_tablet_list_Form(request.POST, request.FILES, instance=post)
            if form.is_valid():
                tablet = form.save(commit=False)
                tablet.dlm = timezone.now()
                tablet.save()
                pk = str(tablet.id)

                # my_custom_sql('''call pda_sp_inHistory ('%s')''' % pk)

                return redirect('/info_about_tablet/' + pk)
        else:
            form = Tbl_tablet_list_Form(instance=post)
    print(my_file)
    arg = {
        'username': username,
        'form': form,
        'my_file': my_file[0][0]
    }
    return render(request, 'inventory/add_new_tablet.html', arg)
