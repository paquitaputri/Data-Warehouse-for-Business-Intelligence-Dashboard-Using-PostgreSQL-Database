from django.urls import path
from sales.views import *

urlpatterns = [
    path('', index, name='sales'),
    path('yearly-sales/', yearly_sales, name='yearly-sales'),
    path('yearly-sales-2015/', yearly_sales_2015, name='yearly-sales-2015'),
    path('yearly-sales-2016/', yearly_sales_2016, name='yearly-sales-2016'),
    path('yearly-sales-2017/', yearly_sales_2017, name='yearly-sales-2017'),
    path('yearly-sales-2018/', yearly_sales_2018, name='yearly-sales-2018'),
    path('quarterly-sales/', quarterly_sales, name='quarterly-sales'),

] 