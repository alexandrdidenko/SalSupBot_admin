from django import forms
from .models import *


class Tbl_tablet_list_Form(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = (
            # 'IMEI_1',
            # 'IMEI_2',
            # 'device_number',
            # 'device_model_id',
            # 'owners_id',
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
            # 'IMEI_1': forms.TextInput(attrs={'placeholder': 'IMEI_1', 'class': 'form-control'}),
            # 'IMEI_2': forms.TextInput(attrs={'class': 'form-control'}),
            # 'device_number': forms.TextInput(attrs={'class': 'form-control'}),
            # 'device_model_id': forms.Select(attrs={'class': 'form-control'}),
            # 'owners_id': forms.Select(attrs={'class': 'form-control'}),
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
