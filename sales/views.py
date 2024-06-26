from django.shortcuts import render, redirect
from django.db import connection
from django.contrib.auth.decorators import login_required
from sales.models import *
from django.db.models import Sum
from django.db.models.functions import TruncYear
from django.views.generic import TemplateView
from sales.queries import *


# Create your views here.
def dictfetchall(cursor):
    desc = cursor.description
    return [
            dict(zip([col[0] for col in desc], row))
            for row in cursor.fetchall()
    ]

@login_required(login_url='login')
def index(request):
    revenue = FaktaPenjualan.objects.all().aggregate(Sum('harga'))
    profit = FaktaPenjualan.objects.all().aggregate(Sum('profit'))
    count = FaktaPenjualan.objects.count()

    cursor = connection.cursor()
    cursor.execute(rollup_category_year_revenue)
    r = dictfetchall(cursor)
    category_revenue_category1 = []
    category_revenue_category2 = []
    category_revenue_category3 = []
    labels_category = []

    for i in range(len(r)):
        if r[i]['tahun'] != None or r[i]['kategori'] != None:
            if r[i]['kategori'] == 'Furniture':
                angka = float(r[i]['revenue'])
                category_revenue_category1.append(angka)
            elif r[i]['kategori'] == 'Office Supplies':
                angka = float(r[i]['revenue'])
                category_revenue_category2.append(angka)
            elif r[i]['kategori'] == 'Technology':
                angka = float(r[i]['revenue'])
                category_revenue_category3.append(angka)
    
    for i in range(len(r)) :
        if r[i]['kategori'] != None :
            if r[i]['kategori'] not in labels_category :
                labels_category.append(r[i]['kategori'])

    cursor.execute(rollup_year_revenue)
    r2 = dictfetchall(cursor)
    label_tahun = []
    data_revenue = []
    for i in range(len(r2)):
        if r2[i]['tahun'] != None :
            label_tahun.append(r2[i]['tahun'])
            angka = float(r2[i]['revenue'])
            data_revenue.append(angka)

    beda_revenue = (data_revenue[len(data_revenue) - 1] - data_revenue[len(data_revenue) - 2])

    cursor.execute(rollup_year_profit)
    r3 = dictfetchall(cursor)
    data_profit = []
    for i in range(len(r3)):
        if r3[i]['tahun'] != None :
            angka = float(r3[i]['profit'])
            data_profit.append(angka)

    beda_profit = (data_profit[len(data_profit) - 1] - data_profit[len(data_profit) - 2])

    cursor.execute(rollup_category_year_profit)
    r4 = dictfetchall(cursor)
    category_profit_category1 = []
    category_profit_category2 = []
    category_profit_category3 = []

    for i in range(len(r4)):
        if r4[i]['tahun'] != None or r4[i]['kategori'] != None:
            if r4[i]['kategori'] == 'Furniture':
                angka = float(r4[i]['profit'])
                category_profit_category1.append(angka)
            elif r4[i]['kategori'] == 'Office Supplies':
                angka = float(r4[i]['profit'])
                category_profit_category2.append(angka)
            elif r4[i]['kategori'] == 'Technology':
                angka = float(r4[i]['profit'])
                category_profit_category3.append(angka)
    
    cursor.execute(region_revenue)
    r5 = dictfetchall(cursor)
    label_region = []
    revenue_region = []

    for i in range(len(r5)):
        if r5[i]['region'] != None:
            label_region.append(r5[i]['region'])
            angka = float(r5[i]['revenue'])
            revenue_region.append(angka)

    cursor.execute(region_profit)
    r6 = dictfetchall(cursor)
    profit_region = []

    for i in range(len(r6)):
        if r6[i]['region'] != None:
            angka = float(r6[i]['profit'])
            profit_region.append(angka)


    content = {
        'revenue' : "{:,}".format(revenue['harga__sum']),
        'profit' : "{:,}".format(profit['profit__sum']),
        'count' : count,
        'label_category' : labels_category,
        'label_tahun' : label_tahun,
        'label_region' : label_region,
        'revenue_year' : data_revenue,
        'beda_revenue' : beda_revenue,
        'profit_year' : data_profit,
        'beda_profit' : beda_profit,
        'revenue_region' : revenue_region,
        'profit_region' : profit_region,
        'revenue_category1' : category_revenue_category1,
        'revenue_category2' : category_revenue_category2,
        'revenue_category3' : category_revenue_category3,
        'profit_category1' : category_profit_category1,
        'profit_category2' : category_profit_category2,
        'profit_category3' : category_profit_category3,
    }

    return render(request, 'sales/sales.html', content)

@login_required(login_url='login')
def yearly_sales(request):
    revenue = FaktaPenjualan.objects.all().aggregate(Sum('harga'))
    profit = FaktaPenjualan.objects.all().aggregate(Sum('profit'))
    count = FaktaPenjualan.objects.count()

    cursor = connection.cursor()
    cursor.execute(rollup_category_year_revenue)
    r = dictfetchall(cursor)
    category_revenue_category1 = []
    category_revenue_category2 = []
    category_revenue_category3 = []
    labels_category = []

    for i in range(len(r)):
        if r[i]['tahun'] != None or r[i]['kategori'] != None:
            if r[i]['kategori'] == 'Furniture':
                angka = float(r[i]['revenue'])
                category_revenue_category1.append(angka)
            elif r[i]['kategori'] == 'Office Supplies':
                angka = float(r[i]['revenue'])
                category_revenue_category2.append(angka)
            elif r[i]['kategori'] == 'Technology':
                angka = float(r[i]['revenue'])
                category_revenue_category3.append(angka)
    
    for i in range(len(r)) :
        if r[i]['kategori'] != None :
            if r[i]['kategori'] not in labels_category :
                labels_category.append(r[i]['kategori'])

    cursor.execute(rollup_year_revenue)
    r2 = dictfetchall(cursor)
    label_tahun = []
    data_revenue = []
    for i in range(len(r2)):
        if r2[i]['tahun'] != None :
            label_tahun.append(r2[i]['tahun'])
            angka = float(r2[i]['revenue'])
            data_revenue.append(angka)

    revenue = data_revenue[len(data_revenue) - 1]       
    beda_revenue = (data_revenue[len(data_revenue) - 1] - data_revenue[len(data_revenue) - 2])

    cursor.execute(rollup_year_profit)
    r3 = dictfetchall(cursor)
    data_profit = []
    for i in range(len(r3)):
        if r3[i]['tahun'] != None :
            angka = float(r3[i]['profit'])
            data_profit.append(angka)

    profit = data_profit[len(data_profit) - 1]
    beda_profit = (data_profit[len(data_profit) - 1] - data_profit[len(data_profit) - 2])

    cursor.execute(rollup_category_year_profit)
    r4 = dictfetchall(cursor)
    category_profit_category1 = []
    category_profit_category2 = []
    category_profit_category3 = []

    for i in range(len(r4)):
        if r4[i]['tahun'] != None or r4[i]['kategori'] != None:
            if r4[i]['kategori'] == 'Furniture':
                angka = float(r4[i]['profit'])
                category_profit_category1.append(angka)
            elif r4[i]['kategori'] == 'Office Supplies':
                angka = float(r4[i]['profit'])
                category_profit_category2.append(angka)
            elif r4[i]['kategori'] == 'Technology':
                angka = float(r4[i]['profit'])
                category_profit_category3.append(angka)

    cursor.execute(rollup_month_revenue)
    r5 = dictfetchall(cursor)
    month_revenue = []

    for i in range(len(r5)):
        if r5[i]['bulan'] != None :
            angka = float(r5[i]['revenue'])
            month_revenue.append(angka)


    cursor.execute(rollup_month_profit)
    r6 = dictfetchall(cursor)
    month_profit = []

    for i in range(len(r6)):
        if r6[i]['bulan'] != None :
            angka = float(r6[i]['profit'])
            month_profit.append(angka)

    cursor.execute(region_revenue)
    r7 = dictfetchall(cursor)
    label_region = []
    revenue_region = []

    for i in range(len(r7)):
        if r7[i]['region'] != None:
            label_region.append(r7[i]['region'])
            angka = float(r7[i]['revenue'])
            revenue_region.append(angka)

    cursor.execute(region_profit)
    r8 = dictfetchall(cursor)
    profit_region = []

    for i in range(len(r8)):
        if r8[i]['region'] != None:
            angka = float(r8[i]['profit'])
            profit_region.append(angka)
    
    content = {
        'revenue' : "{:,}".format(revenue),
        'profit' : "{:,}".format(profit),
        'count' : count,
        'label_category' : labels_category,
        'label_tahun' : label_tahun,
        'label_region' : label_region,
        'revenue_year' : data_revenue,
        'beda_revenue' : beda_revenue,
        'profit_year' : data_profit, 
        'beda_profit' : beda_profit,
        'revenue_region' : revenue_region,
        'profit_region' : profit_region,
        'revenue_category1' : category_revenue_category1,
        'revenue_category2' : category_revenue_category2,
        'revenue_category3' : category_revenue_category3,
        'profit_category1' : category_profit_category1,
        'profit_category2' : category_profit_category2,
        'profit_category3' : category_profit_category3
    }

    return render(request, 'sales/sales-yearly.html', content)

@login_required(login_url='login')    
def yearly_sales_2015(request):

    cursor = connection.cursor()
    cursor.execute(rollup_month_revenue)
    r = dictfetchall(cursor)
    label_bulan = []
    label_tahun = []
    revenue_tahun1 = []

    for i in range(len(r)) :
        if r[i]['tahun'] not in label_tahun :
            if r[i]['tahun'] != None:
                label_tahun.append(r[i]['tahun'])

    for i in range(len(r)):
        if r[i]['bulan'] not in label_bulan :
            if r[i]['bulan'] != None:
                label_bulan.append(r[i]['bulan'])
    
    for i in range(len(r)):
        if r[i]['tahun'] == '2015' and r[i]['bulan'] != None:
            angka = float(r[i]['revenue'])
            revenue_tahun1.append(angka)

    cursor.execute(rollup_category_month_revenue)
    r2 = dictfetchall(cursor)

    revenue1_category1 = []
    revenue1_category2 = []
    revenue1_category3 = []

    label_category = []
    

    for i in range(len(r2)) :
        if r2[i]['kategori'] != None :
            if r2[i]['kategori'] not in label_category :
                label_category.append(r2[i]['kategori'])

    for i in range(len(r2)):
        if r2[i]['tahun'] != None and r2[i]['kategori'] != None:
            if r2[i]['tahun'] == '2015' and r2[i]['kategori'] == 'Furniture':
                angka = float(r2[i]['revenue'])
                revenue1_category1.append(angka)
            elif r2[i]['tahun'] == '2015' and r2[i]['kategori'] == 'Office Supplies':
                angka = float(r2[i]['revenue'])
                revenue1_category2.append(angka)
            elif r2[i]['tahun'] == '2015' and r2[i]['kategori'] == 'Technology':
                angka = float(r2[i]['revenue'])
                revenue1_category3.append(angka)
    
    cursor.execute(rollup_category_month_profit)
    r3 = dictfetchall(cursor)

    profit1_category1 = []
    profit1_category2 = []
    profit1_category3 = []


    for i in range(len(r3)) :
        if r3[i]['kategori'] != None :
            if r3[i]['kategori'] not in label_category :
                label_category.append(r3[i]['kategori'])

    for i in range(len(r3)):
        if r3[i]['tahun'] != None and r2[i]['bulan'] != None and r3[i]['kategori'] != None:
            if r3[i]['tahun'] == '2015':
                if r3[i]['tahun'] == '2015' and r3[i]['kategori'] == 'Furniture':
                    angka = float(r3[i]['profit'])
                    profit1_category1.append(angka)
                elif r3[i]['tahun'] == '2015' and r3[i]['kategori'] == 'Office Supplies':
                    angka = float(r3[i]['profit'])
                    profit1_category2.append(angka)
                elif r3[i]['tahun'] == '2015' and r3[i]['kategori'] == 'Technology':
                    angka = float(r3[i]['profit'])
                    profit1_category3.append(angka)

    cursor.execute(rollup_month_profit)
    r4 = dictfetchall(cursor)
    
    profit_tahun1 = []

    for i in range(len(r4)):
        if r4[i]['tahun'] == '2015' and r4[i]['bulan'] != None:
            angka = float(r4[i]['profit'])
            profit_tahun1.append(angka)

    cursor.execute(rollup_year_revenue)
    r5 = dictfetchall(cursor)
    revenue = 0
    for i in range(len(r5)):
        if r5[i]['tahun'] == '2015':
            revenue += float(r5[i]['revenue'])
            str_revenue = '{0:,}'.format(revenue)

    cursor.execute(rollup_year_profit)
    r6 = dictfetchall(cursor)
    profit = 0
    for i in range(len(r6)):
        if r6[i]['tahun'] == '2015':
            profit += float(r6[i]['profit'])
            str_profit = '{0:,}'.format(profit)

    cursor.execute(transaksi_year)
    r7 = dictfetchall(cursor)
    transaksi = 0
    for i in range(len(r7)):
        if r7[i]['tahun'] == '2015':
            transaksi += int(r7[i]['transaksi'])
    
    cursor.execute(region_revenue_2015)
    r8 = dictfetchall(cursor)
    label_region = []
    revenue_region = []

    for i in range(len(r8)):
        if r8[i]['tahun'] and r8[i]['region'] != None:
            label_region.append(r8[i]['region'])
            revenue_region.append(float(r8[i]['revenue'])) 

    cursor.execute(region_profit_2015)
    r9 = dictfetchall(cursor)
    profit_region = []
    for i in range(len(r9)):
        if r9[i]['tahun'] and r9[i]['region'] != None:
            profit_region.append(float(r9[i]['profit'])) 

    content = {
        'label_tahun' : label_tahun,
        'label_bulan' : label_bulan,
        'label_category' : label_category,
        'label_region' : label_region,
        'revenue_category1' : revenue1_category1,
        'revenue_category2' : revenue1_category2,
        'revenue_category3' : revenue1_category3,
        'revenue_tahun1' : revenue_tahun1,
        'revenue' : str_revenue,
        'profit' : str_profit,
        'revenue_region' : revenue_region,
        'profit_region' : profit_region,
        'count' : transaksi,
        'profit_category1' : profit1_category1,
        'profit_category2' : profit1_category2,
        'profit_category3' : profit1_category3,
        'profit_tahun1' : profit_tahun1
    }


    return render(request, 'sales/yearly/sales-yearly-2015.html', content)

@login_required(login_url='login')
def yearly_sales_2016(request):

    cursor = connection.cursor()
    cursor.execute(rollup_month_revenue)
    r = dictfetchall(cursor)
    label_bulan = []
    label_tahun = []

    revenue_tahun2 = []

    for i in range(len(r)) :
        if r[i]['tahun'] not in label_tahun :
            if r[i]['tahun'] != None:
                label_tahun.append(r[i]['tahun'])

    for i in range(len(r)):
        if r[i]['bulan'] not in label_bulan :
            if r[i]['bulan'] != None:
                label_bulan.append(r[i]['bulan'])
    
    for i in range(len(r)):
        if r[i]['tahun'] == '2016' and r[i]['bulan'] != None:
            angka = float(r[i]['revenue'])
            revenue_tahun2.append(angka)

     

    cursor.execute(rollup_category_month_revenue)
    r2 = dictfetchall(cursor)

    revenue2_category1 = []
    revenue2_category2 = []
    revenue2_category3 = []

    label_category = []
    

    for i in range(len(r2)) :
        if r2[i]['kategori'] != None :
            if r2[i]['kategori'] not in label_category :
                label_category.append(r2[i]['kategori'])

    for i in range(len(r2)):
        if r2[i]['tahun'] != None and r2[i]['kategori'] != None:
            if r2[i]['tahun'] == '2016' and r2[i]['kategori'] == 'Furniture':
                angka = float(r2[i]['revenue'])
                revenue2_category1.append(angka)
            elif r2[i]['tahun'] == '2016' and r2[i]['kategori'] == 'Office Supplies':
                angka = float(r2[i]['revenue'])
                revenue2_category2.append(angka)
            elif r2[i]['tahun'] == '2016' and r2[i]['kategori'] == 'Technology':
                angka = float(r2[i]['revenue'])
                revenue2_category3.append(angka)

    
    cursor.execute(rollup_category_month_profit)
    r3 = dictfetchall(cursor)

    profit2_category1 = []
    profit2_category2 = []
    profit2_category3 = []
    

    for i in range(len(r3)) :
        if r3[i]['kategori'] != None :
            if r3[i]['kategori'] not in label_category :
                label_category.append(r3[i]['kategori'])

    for i in range(len(r3)):
        if r3[i]['tahun'] != None and r2[i]['bulan'] != None and r3[i]['kategori'] != None:
            if r3[i]['tahun'] == '2016':
                if r3[i]['tahun'] == '2016' and r3[i]['kategori'] == 'Furniture':
                    angka = float(r3[i]['profit'])
                    profit2_category1.append(angka)
                elif r3[i]['tahun'] == '2016' and r3[i]['kategori'] == 'Office Supplies':
                    angka = float(r3[i]['profit'])
                    profit2_category2.append(angka)
                elif r3[i]['tahun'] == '2016' and r3[i]['kategori'] == 'Technology':
                    angka = float(r3[i]['profit'])
                    profit2_category3.append(angka)


    cursor = connection.cursor()
    cursor.execute(rollup_month_profit)
    r4 = dictfetchall(cursor)
    
    profit_tahun2 = []

    for i in range(len(r4)):
        if r4[i]['tahun'] == '2016' and r4[i]['bulan'] != None:
            angka = float(r4[i]['profit'])
            profit_tahun2.append(angka)

    cursor.execute(rollup_year_revenue)
    r5 = dictfetchall(cursor)
    revenue = 0
    for i in range(len(r5)):
        if r5[i]['tahun'] == '2016':
            revenue += float(r5[i]['revenue'])
            str_revenue = '{0:,}'.format(revenue)

    cursor.execute(rollup_year_profit)
    r6 = dictfetchall(cursor)
    profit = 0
    for i in range(len(r6)):
        if r6[i]['tahun'] == '2016':
            profit += float(r6[i]['profit'])
            str_profit = '{0:,}'.format(profit)

    cursor.execute(transaksi_year)
    r7 = dictfetchall(cursor)
    transaksi = 0
    for i in range(len(r7)):
        if r7[i]['tahun'] == '2016':
            transaksi += int(r7[i]['transaksi'])
    
    cursor.execute(region_revenue_2016)
    r8 = dictfetchall(cursor)
    label_region = []
    revenue_region = []

    for i in range(len(r8)):
        if r8[i]['tahun'] and r8[i]['region'] != None:
            label_region.append(r8[i]['region'])
            revenue_region.append(float(r8[i]['revenue'])) 

    cursor.execute(region_profit_2016)
    r9 = dictfetchall(cursor)
    profit_region = []
    for i in range(len(r9)):
        if r9[i]['tahun'] and r9[i]['region'] != None:
            profit_region.append(float(r9[i]['profit'])) 

    content = {
        'label_tahun' : label_tahun,
        'label_bulan' : label_bulan,
        'label_category' : label_category,
        'label_region' : label_region,
        'revenue_category1' : revenue2_category1,
        'revenue_category2' : revenue2_category2,
        'revenue_category3' : revenue2_category3,
        'revenue_tahun2' : revenue_tahun2,
        'revenue' : str_revenue,
        'profit' : str_profit,
        'revenue_region' : revenue_region,
        'profit_region' : profit_region,
        'count' : transaksi,
        'profit_category1' : profit2_category1,
        'profit_category2' : profit2_category2,
        'profit_category3' : profit2_category3,
        'profit_tahun2' : profit_tahun2
    }

    return render(request, 'sales/yearly/sales-yearly-2016.html', content)

@login_required(login_url='login')
def yearly_sales_2017(request):
    
    cursor = connection.cursor()
    cursor.execute(rollup_month_revenue)
    r = dictfetchall(cursor)
    label_bulan = []
    label_tahun = []

    revenue_tahun3 = []

    for i in range(len(r)) :
        if r[i]['tahun'] not in label_tahun :
            if r[i]['tahun'] != None:
                label_tahun.append(r[i]['tahun'])

    for i in range(len(r)):
        if r[i]['bulan'] not in label_bulan :
            if r[i]['bulan'] != None:
                label_bulan.append(r[i]['bulan'])
    
    for i in range(len(r)):
        if r[i]['tahun'] == '2017' and r[i]['bulan'] != None:
            angka = float(r[i]['revenue'])
            revenue_tahun3.append(angka)

     

    cursor.execute(rollup_category_month_revenue)
    r2 = dictfetchall(cursor)

    revenue3_category1 = []
    revenue3_category2 = []
    revenue3_category3 = []

    label_category = []
    

    for i in range(len(r2)) :
        if r2[i]['kategori'] != None :
            if r2[i]['kategori'] not in label_category :
                label_category.append(r2[i]['kategori'])

    for i in range(len(r2)):
        if r2[i]['tahun'] != None and r2[i]['kategori'] != None:
            if r2[i]['tahun'] == '2017' and r2[i]['kategori'] == 'Furniture':
                angka = float(r2[i]['revenue'])
                revenue3_category1.append(angka)
            elif r2[i]['tahun'] == '2017' and r2[i]['kategori'] == 'Office Supplies':
                angka = float(r2[i]['revenue'])
                revenue3_category2.append(angka)
            elif r2[i]['tahun'] == '2017' and r2[i]['kategori'] == 'Technology':
                angka = float(r2[i]['revenue'])
                revenue3_category3.append(angka)

    
    cursor.execute(rollup_category_month_profit)
    r3 = dictfetchall(cursor)

    profit3_category1 = []
    profit3_category2 = []
    profit3_category3 = []
    

    for i in range(len(r3)) :
        if r3[i]['kategori'] != None :
            if r3[i]['kategori'] not in label_category :
                label_category.append(r3[i]['kategori'])

    for i in range(len(r3)):
        if r3[i]['tahun'] != None and r2[i]['bulan'] != None and r3[i]['kategori'] != None:
            if r3[i]['tahun'] == '2017':
                if r3[i]['tahun'] == '2017' and r3[i]['kategori'] == 'Furniture':
                    angka = float(r3[i]['profit'])
                    profit3_category1.append(angka)
                elif r3[i]['tahun'] == '2017' and r3[i]['kategori'] == 'Office Supplies':
                    angka = float(r3[i]['profit'])
                    profit3_category2.append(angka)
                elif r3[i]['tahun'] == '2017' and r3[i]['kategori'] == 'Technology':
                    angka = float(r3[i]['profit'])
                    profit3_category3.append(angka)


    cursor = connection.cursor()
    cursor.execute(rollup_month_profit)
    r4 = dictfetchall(cursor)
    
    profit_tahun3 = []

    for i in range(len(r4)):
        if r4[i]['tahun'] == '2017' and r4[i]['bulan'] != None:
            angka = float(r4[i]['profit'])
            profit_tahun3.append(angka)

    cursor.execute(rollup_year_revenue)
    r5 = dictfetchall(cursor)
    revenue = 0
    for i in range(len(r5)):
        if r5[i]['tahun'] == '2017':
            revenue += float(r5[i]['revenue'])
            str_revenue = '{0:,}'.format(revenue)

    cursor.execute(rollup_year_profit)
    r6 = dictfetchall(cursor)
    profit = 0
    for i in range(len(r6)):
        if r6[i]['tahun'] == '2017':
            profit += float(r6[i]['profit'])
            str_profit = '{0:,}'.format(profit)

    cursor.execute(transaksi_year)
    r7 = dictfetchall(cursor)
    transaksi = 0
    for i in range(len(r7)):
        if r7[i]['tahun'] == '2017':
            transaksi += int(r7[i]['transaksi'])
    
    cursor.execute(region_revenue_2017)
    r8 = dictfetchall(cursor)
    label_region = []
    revenue_region = []

    for i in range(len(r8)):
        if r8[i]['tahun'] and r8[i]['region'] != None:
            label_region.append(r8[i]['region'])
            revenue_region.append(float(r8[i]['revenue'])) 

    cursor.execute(region_profit_2017)
    r9 = dictfetchall(cursor)
    profit_region = []
    for i in range(len(r9)):
        if r9[i]['tahun'] and r9[i]['region'] != None:
            profit_region.append(float(r9[i]['profit'])) 

    content = {
        'label_tahun' : label_tahun,
        'label_bulan' : label_bulan,
        'label_category' : label_category,
        'label_region' : label_region,
        'revenue_category1' : revenue3_category1,
        'revenue_category2' : revenue3_category2,
        'revenue_category3' : revenue3_category3,
        'revenue_tahun3' : revenue_tahun3,
        'revenue' : str_revenue,
        'profit' : str_profit,
        'revenue_region' : revenue_region,
        'profit_region' : profit_region,
        'count' : transaksi,
        'profit_category1' : profit3_category1,
        'profit_category2' : profit3_category2,
        'profit_category3' : profit3_category3,
        'profit_tahun3' : profit_tahun3
    }

    return render(request, 'sales/yearly/sales-yearly-2017.html', content)

@login_required(login_url='login')
def yearly_sales_2018(request):
    
    cursor = connection.cursor()
    cursor.execute(rollup_month_revenue)
    r = dictfetchall(cursor)
    label_bulan = []
    label_tahun = []

    revenue_tahun4 = []

    for i in range(len(r)) :
        if r[i]['tahun'] not in label_tahun :
            if r[i]['tahun'] != None:
                label_tahun.append(r[i]['tahun'])

    for i in range(len(r)):
        if r[i]['bulan'] not in label_bulan :
            if r[i]['bulan'] != None:
                label_bulan.append(r[i]['bulan'])
    
    for i in range(len(r)):
        if r[i]['tahun'] == '2018' and r[i]['bulan'] != None:
            angka = float(r[i]['revenue'])
            revenue_tahun4.append(angka)

     

    cursor.execute(rollup_category_month_revenue)
    r2 = dictfetchall(cursor)

    revenue4_category1 = []
    revenue4_category2 = []
    revenue4_category3 = []

    label_category = []
    

    for i in range(len(r2)) :
        if r2[i]['kategori'] != None :
            if r2[i]['kategori'] not in label_category :
                label_category.append(r2[i]['kategori'])

    for i in range(len(r2)):
        if r2[i]['tahun'] != None and r2[i]['kategori'] != None:
            if r2[i]['tahun'] == '2018' and r2[i]['kategori'] == 'Furniture':
                angka = float(r2[i]['revenue'])
                revenue4_category1.append(angka)
            elif r2[i]['tahun'] == '2018' and r2[i]['kategori'] == 'Office Supplies':
                angka = float(r2[i]['revenue'])
                revenue4_category2.append(angka)
            elif r2[i]['tahun'] == '2018' and r2[i]['kategori'] == 'Technology':
                angka = float(r2[i]['revenue'])
                revenue4_category3.append(angka)

    
    cursor.execute(rollup_category_month_profit)
    r3 = dictfetchall(cursor)

    profit4_category1 = []
    profit4_category2 = []
    profit4_category3 = []
    

    for i in range(len(r3)) :
        if r3[i]['kategori'] != None :
            if r3[i]['kategori'] not in label_category :
                label_category.append(r3[i]['kategori'])

    for i in range(len(r3)):
        if r3[i]['tahun'] != None and r2[i]['bulan'] != None and r3[i]['kategori'] != None:
            if r3[i]['tahun'] == '2018':
                if r3[i]['tahun'] == '2018' and r3[i]['kategori'] == 'Furniture':
                    angka = float(r3[i]['profit'])
                    profit4_category1.append(angka)
                elif r3[i]['tahun'] == '2018' and r3[i]['kategori'] == 'Office Supplies':
                    angka = float(r3[i]['profit'])
                    profit4_category2.append(angka)
                elif r3[i]['tahun'] == '2018' and r3[i]['kategori'] == 'Technology':
                    angka = float(r3[i]['profit'])
                    profit4_category3.append(angka)


    cursor = connection.cursor()
    cursor.execute(rollup_month_profit)
    r4 = dictfetchall(cursor)
    
    profit_tahun4 = []

    for i in range(len(r4)):
        if r4[i]['tahun'] == '2018' and r4[i]['bulan'] != None:
            angka = float(r4[i]['profit'])
            profit_tahun4.append(angka)

    cursor.execute(rollup_year_revenue)
    r5 = dictfetchall(cursor)
    revenue = 0
    for i in range(len(r5)):
        if r5[i]['tahun'] == '2018':
            revenue += float(r5[i]['revenue'])
            str_revenue = '{0:,}'.format(revenue)

    cursor.execute(rollup_year_profit)
    r6 = dictfetchall(cursor)
    profit = 0
    for i in range(len(r6)):
        if r6[i]['tahun'] == '2018':
            profit += float(r6[i]['profit'])
            str_profit = '{0:,}'.format(profit)

    cursor.execute(transaksi_year)
    r7 = dictfetchall(cursor)
    transaksi = 0
    for i in range(len(r7)):
        if r7[i]['tahun'] == '2018':
            transaksi += int(r7[i]['transaksi'])
    
    cursor.execute(region_revenue_2018)
    r8 = dictfetchall(cursor)
    label_region = []
    revenue_region = []

    for i in range(len(r8)):
        if r8[i]['tahun'] and r8[i]['region'] != None:
            label_region.append(r8[i]['region'])
            revenue_region.append(float(r8[i]['revenue'])) 

    cursor.execute(region_profit_2018)
    r9 = dictfetchall(cursor)
    profit_region = []
    for i in range(len(r9)):
        if r9[i]['tahun'] and r9[i]['region'] != None:
            profit_region.append(float(r9[i]['profit'])) 

    content = {
        'label_tahun' : label_tahun,
        'label_bulan' : label_bulan,
        'label_category' : label_category,
        'label_region' : label_region,
        'revenue_category1' : revenue4_category1,
        'revenue_category2' : revenue4_category2,
        'revenue_category3' : revenue4_category3,
        'revenue_tahun4' : revenue_tahun4,
        'revenue' : str_revenue,
        'profit' : str_profit,
        'revenue_region' : revenue_region,
        'profit_region' : profit_region,
        'count' : transaksi,
        'profit_category1' : profit4_category1,
        'profit_category2' : profit4_category2,
        'profit_category3' : profit4_category3,
        'profit_tahun4' : profit_tahun4
    }

    return render(request, 'sales/yearly/sales-yearly-2018.html', content)

@login_required(login_url='login')
def quarterly_sales(request):
    
    count = FaktaPenjualan.objects.count()
    
    cursor = connection.cursor()
    cursor.execute(rollup_quarterly_revenue)
    r = dictfetchall(cursor)
    quarterly_revenue = []
    label_quarter = []
    label_tahun = []

    quarter_revenue1 = []
    quarter_revenue2 = []
    quarter_revenue3 = []
    quarter_revenue4 = []

    for i in range(len(r)):
        if r[i]['tahun'] != None and r[i]['quarter'] != None :
            angka = float(r[i]['revenue'])
            quarterly_revenue.append(angka)

    for i in range(len(r)):
        if r[i]['tahun'] not in label_tahun and r[i]['tahun'] != None :
            label_tahun.append(r[i]['tahun'])
    
    for i in range(len(r)):
        if r[i]['quarter'] not in label_quarter and r[i]['quarter'] != None :
            label_quarter.append(r[i]['quarter'])

    quarter_revenue = quarterly_revenue[len(quarterly_revenue) - 1]
    difference_revenue = quarterly_revenue[len(quarterly_revenue) - 1] - quarterly_revenue[len(quarterly_revenue) - 2]

    for i in range(len(r)):
        if r[i]['quarter'] != None :
            if r[i]['tahun'] == label_tahun[0]:
                angka = float(r[i]['revenue'])
                quarter_revenue1.append(angka)
            elif r[i]['tahun'] == label_tahun[1]:
                angka = float(r[i]['revenue'])
                quarter_revenue2.append(angka)
            elif r[i]['tahun'] == label_tahun[2]:
                angka = float(r[i]['revenue'])
                quarter_revenue3.append(angka)
            elif r[i]['tahun'] == label_tahun[3]:
                angka = float(r[i]['revenue'])
                quarter_revenue4.append(angka)  


    cursor.execute(rollup_quarterly_profit)
    r2 = dictfetchall(cursor)
    quarterly_profit = []

    for i in range(len(r2)):
        if r2[i]['tahun'] != None and r2[i]['quarter'] != None :
            angka = float(r2[i]['profit'])
            quarterly_profit.append(angka)
    
    quarter_profit = quarterly_profit[len(quarterly_profit) - 1]
    difference_profit = quarterly_profit[len(quarterly_profit) - 1] - quarterly_profit[len(quarterly_profit) - 2]

    quarter_profit1 = []
    quarter_profit2 = []
    quarter_profit3 = []
    quarter_profit4 = []
    
    for i in range(len(r2)):
        if r2[i]['quarter'] != None :
            if r2[i]['tahun'] == label_tahun[0]:
                angka = float(r2[i]['profit'])
                quarter_profit1.append(angka)
            elif r2[i]['tahun'] == label_tahun[1]:
                angka = float(r2[i]['profit'])
                quarter_profit2.append(angka)
            elif r2[i]['tahun'] == label_tahun[2]:
                angka = float(r2[i]['profit'])
                quarter_profit3.append(angka)
            elif r2[i]['tahun'] == label_tahun[3]:
                angka = float(r2[i]['profit'])
                quarter_profit4.append(angka)            
            


    content = {
        'count' : count,
        'quarter' : label_quarter,
        'tahun' : label_tahun,
        'revenue' : quarterly_revenue,
        'profit' : quarterly_profit,
        'quarter_revenue' : "{:,}".format(quarter_revenue),
        'quarter_profit' : "{:,}".format(quarter_profit),
        'perbedaan_revenue' : difference_revenue,
        'revenue_quarter1' : quarter_revenue1, 
        'revenue_quarter2' : quarter_revenue2,
        'revenue_quarter3' : quarter_revenue3,
        'revenue_quarter4' : quarter_revenue4,
        'perbedaan_profit' : difference_profit,
        'profit_quarter1' : quarter_profit1,
        'profit_quarter2' : quarter_profit2,
        'profit_quarter3' : quarter_profit3,
        'profit_quarter4' : quarter_profit4
    }

    return render(request, 'sales/sales-quarterly.html', content)
