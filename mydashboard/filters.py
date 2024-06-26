import django_filters

from sales.models import *

class SalesFilter(django_filters.FilterSet):
    kota = django_filters.CharFilter(field_name='kota__kota_name', lookup_expr='icontains')
    class Meta:
        model = FaktaPenjualan
        fields = ['kota__provinsi__negara__region__nama_region', 'segmen__nama_segmen', 'pelanggan__nama_pelanggan', 'pesanan']

class SalesFilter2(django_filters.FilterSet):
    class Meta:
        model = FaktaPenjualan
        fields = ['pesanan']