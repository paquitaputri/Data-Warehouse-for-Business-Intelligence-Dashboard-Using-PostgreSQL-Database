from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from sales.models import *
from logistic.models import *

class DateInput(forms.DateInput):
    input_type = 'date'

class OrderPenjualan(ModelForm):
    class Meta:
        model = FaktaPenjualan
        fields = ['pesanan', 'kota', 'tanggal_pesanan','pelanggan', 'segmen', 'harga', 'profit', 'jumlah_barang']
    tanggal_pesanan = forms.DateTimeField(widget=DateInput)
    jumlah_barang = forms.IntegerField()


class UserFormRegister(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2'] 

