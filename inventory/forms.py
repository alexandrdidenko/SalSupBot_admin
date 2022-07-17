from django import forms
from .models import *


class Tbl_tablet_list_Form(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = (
            'model',
            'sn',
            'imei1',
            'imei2',
            'check_info',
            'file_name'
            # 'customers_cust_id',
            # 'who_uses',
            # 'purchase_date',
            # 'coment',
            # 'technical_condition_id',
            # 'Decommissioning_date',
            # 'ssc_id',
            # 'obd_id',
        )
        widgets = {
            'model': forms.TextInput(attrs={'placeholder': 'model', 'class': 'form-control'}),
            'sn': forms.TextInput(attrs={'class': 'form-control'}),
            'imei1': forms.TextInput(attrs={'class': 'form-control'}),
            'imei2': forms.TextInput(attrs={'class': 'form-control'}),
            'check_info': forms.TextInput(attrs={'class': 'form-control'}),
            'file_name': forms.FileInput()
            # 'customers_cust_id': forms.Select(attrs={'class': 'form-control'}),
            # 'who_uses': forms.Select(attrs={'class': 'form-control'}),
            # 'purchase_date': forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD', 'class': 'form-control'}),
            # 'coment': forms.TextInput(attrs={'class': 'form-control'}),
            # 'technical_condition_id': forms.Select(attrs={'class': 'form-control'}),
            # 'Decommissioning_date': forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD', 'class': 'form-control'}),
            # 'ssc_id': forms.Select(attrs={'class': 'form-control'}),
            # 'obd_id': forms.Select(attrs={'class': 'form-control'}),


        }

        labels = {
            # 'IMEI_1': 'IMEI 1 номер',
            # 'IMEI_2': 'IMEI 2 номер',
        }
