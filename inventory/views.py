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


def all_tablets_view(request):
    username = auth.get_user(request)

    if username.is_anonymous:
        username = ''
        return redirect('/logon')
    else:
        all_tablets = Inventory.objects.raw('select TOP 30 * from [bot].[bot_inventory]')
        arg = {
            'username': username,
            'all_tablets': all_tablets,
        }
        return render(request, 'inventory/all_tablets.html', arg)
