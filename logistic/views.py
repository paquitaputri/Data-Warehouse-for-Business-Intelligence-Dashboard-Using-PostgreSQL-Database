import pandas as pd
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import connection
from django.contrib.auth.decorators import login_required
from logistic.models import *
from logistic.queries import *
# Create your views here.

# Create your views here.
def dictfetchall(cursor):
    desc = cursor.description
    return [
            dict(zip([col[0] for col in desc], row))
            for row in cursor.fetchall()
    ]

@login_required(login_url='login')
def index(request):
    cursor = connection.cursor()
    cursor.execute(rollup_ontime_year)
    r = dictfetchall(cursor)

    label_tahun = []
    ontime_year = []


    for i in range(len(r)):
        if r[i]['tahun'] != None:
            ontime_year.append(r[i]['on_time'])
            if r[i]['tahun'] not in label_tahun:
                label_tahun.append(r[i]['tahun'])
        else:
            total_ontime=r[i]['on_time']

    cursor.execute(rollup_infull_year)
    r2 = dictfetchall(cursor)

    infull_year = []

    for i in range(len(r2)):
        if r2[i]['tahun'] != None :
            infull_year.append(r2[i]['in_full'])
        else:
            total_infull=r2[i]['in_full']


    cursor.execute(rollup_otif_year)
    r3 = dictfetchall(cursor)

    otif_year = []

    for i in range(len(r3)):
        if r3[i]['tahun'] != None :
            otif_year.append(r3[i]['otif'])
        else:
            total_otif=r3[i]['otif']

    cursor.execute(pengiriman_rollup_year)
    r4 = dictfetchall(cursor)

    transaksi_year = []

    for i in range(len(r4)):
        if r4[i]['tahun'] != None :
            transaksi_year.append(r4[i]['transaksi'])
        else:
            total_transaksi=r4[i]['transaksi']
    

    percent_otif_year = []
    for i in range(len(transaksi_year)):
        percent_otif_year.append(round(((otif_year[i] / transaksi_year[i]) * 100), 2))
    
    kpi_otif = round(((total_otif / total_transaksi)*100), 2)

    cursor=connection.cursor()
    cursor.execute(rollup_category_otif)
    r5=dictfetchall(cursor)

    otif_category1 = []
    otif_category2 = []
    otif_category3 = []
    label_category = []
    label_tahun = []

    for i in range(len(r5)):
        if r5[i]['kategori'] != None:
            label_category.append(r5[i]['kategori'])

    for i in range(len(r5)):
        if r5[i]['tahun'] != None:
            if r5[i]['tahun'] not in label_tahun:
                label_tahun.append(r5[i]['tahun'])

    for i in range(len(r5)):
        if r5[i]['kategori'] == 'Furniture' :
            otif_category1.append(r5[i]['otif'])

    for i in range(len(r5)):
        if r5[i]['kategori'] == 'Office Supplies' :
            otif_category2.append(r5[i]['otif'])

    for i in range(len(r5)):
        if r5[i]['kategori'] == 'Technology' :
            otif_category3.append(r5[i]['otif'])   

    cursor=connection.cursor()
    cursor.execute(rollup_category_pengiriman)
    r6=dictfetchall(cursor)

    pengiriman_category1 = []
    pengiriman_category2 = []
    pengiriman_category3 = []
    
    for i in range(len(r6)):
        if r6[i]['kategori'] == 'Furniture' :
            pengiriman_category1.append(r6[i]['jumlah_pengiriman'])

    for i in range(len(r6)):
        if r6[i]['kategori'] == 'Office Supplies' :
            pengiriman_category2.append(r6[i]['jumlah_pengiriman'])

    for i in range(len(r6)):
        if r6[i]['kategori'] == 'Technology' :
            pengiriman_category3.append(r6[i]['jumlah_pengiriman'])  

    percent_otif_category1 = []
    percent_otif_category2 = []
    percent_otif_category3 = []

    for i in range(len(label_tahun)):
        percent_otif_category1.append(round(((otif_category1[i] /  pengiriman_category1[i]) * 100), 2))

    for i in range(len(label_tahun)):
        percent_otif_category2.append(round(((otif_category2[i] /  pengiriman_category2[i]) * 100), 2))

    for i in range(len(label_tahun)):
        percent_otif_category3.append(round(((otif_category3[i] /  pengiriman_category3[i]) * 100), 2))

    cursor=connection.cursor()
    cursor.execute(rollup_region_otif_per_year)
    r7=dictfetchall(cursor)

    otif_region1 = []
    otif_region2 = []
    otif_region3 = []
    label_region = []

    for i in range(len(r7)):
        if r7[i]['region'] != None:
            label_region.append(r7[i]['region'])

    for i in range(len(r7)):
        if r7[i]['region'] == 'Central' :
            otif_region1.append(r7[i]['otif'])

    for i in range(len(r7)):
        if r7[i]['region'] == 'North' :
            otif_region2.append(r7[i]['otif'])

    for i in range(len(r7)):
        if r7[i]['region'] == 'South' :
            otif_region3.append(r7[i]['otif'])   

    cursor=connection.cursor()
    cursor.execute(rollup_region_pengiriman)
    r8=dictfetchall(cursor)

    pengiriman_region1 = []
    pengiriman_region2 = []
    pengiriman_region3 = []
    
    for i in range(len(r8)):
        if r8[i]['region'] == 'Central' :
            pengiriman_region1.append(r8[i]['jumlah_pengiriman'])

    for i in range(len(r8)):
        if r8[i]['region'] == 'North' :
            pengiriman_region2.append(r8[i]['jumlah_pengiriman'])

    for i in range(len(r8)):
        if r8[i]['region'] == 'South' :
            pengiriman_region3.append(r8[i]['jumlah_pengiriman'])  

    percent_otif_region1 = []
    percent_otif_region2 = []
    percent_otif_region3 = []

    for i in range(len(label_tahun)):
        percent_otif_region1.append(round(((otif_region1[i] /  pengiriman_region1[i]) * 100), 2))

    for i in range(len(label_tahun)):
        percent_otif_region2.append(round(((otif_region2[i] /  pengiriman_region2[i]) * 100), 2))

    for i in range(len(label_tahun)):
        percent_otif_region3.append(round(((otif_region3[i] /  pengiriman_region3[i]) * 100), 2))

    content = {
        'data_ontime' : ontime_year,
        'data_infull' : infull_year,
        'data_transaksi' : transaksi_year,
        'data_percent_otif' : percent_otif_year,
        'total_transaksi' : total_transaksi,
        'total_ontime' : total_ontime,
        'total_infull' : total_infull, 
        'kpi_otif' : kpi_otif,
        'label_tahun' : label_tahun,
        'label_category' : label_category,
        'label_region' : label_region,
        'category1' : percent_otif_category1,
        'category2' : percent_otif_category2,
        'category3' : percent_otif_category3,
        'region1' : percent_otif_region1,
        'region2' : percent_otif_region2,
        'region3' : percent_otif_region3,
        
    }
    return render(request, 'logistic/logistic.html', content)

@login_required(login_url='login')
def logistic_yearly(request):

    cursor = connection.cursor()
    cursor.execute(rollup_ontime_year)
    r = dictfetchall(cursor)

    label_tahun = []
    ontime_year = []

    for i in range(len(r)):
        if r[i]['tahun'] != None:
            ontime_year.append(r[i]['on_time'])
            if r[i]['tahun'] not in label_tahun:
                label_tahun.append(r[i]['tahun'])

    last_ontime = ontime_year[len(ontime_year) - 1]
    different_ontime = (ontime_year[len(ontime_year) - 1] - ontime_year[len(ontime_year) - 2])
    last_year = label_tahun[len(label_tahun) - 2]

    cursor.execute(rollup_infull_year)
    r2 = dictfetchall(cursor)

    infull_year = []

    for i in range(len(r2)):
        if r2[i]['tahun'] != None :
            infull_year.append(r2[i]['in_full'])

    last_infull = infull_year[len(infull_year) - 1]
    different_infull = (infull_year[len(infull_year) - 1] - infull_year[len(infull_year) - 2])

    cursor.execute(rollup_otif_year)
    r3 = dictfetchall(cursor)

    otif_year = []

    for i in range(len(r3)):
        if r3[i]['tahun'] != None :
            otif_year.append(r3[i]['otif'])
        else:
            total_otif = r3[i]['otif']

    cursor.execute(pengiriman_rollup_year)
    r4 = dictfetchall(cursor)

    transaksi_year = []

    for i in range(len(r4)):
        if r4[i]['tahun'] != None :
            transaksi_year.append(r4[i]['transaksi'])
        else:
            total_transaksi = r4[i]['transaksi']
    
    last_transaksi = transaksi_year[len(transaksi_year) - 1]
    different_transaksi = (transaksi_year[len(transaksi_year) - 1] - transaksi_year[len(transaksi_year) - 2])

    percent_otif_year = []
    for i in range(len(transaksi_year)):
        percent_otif_year.append(round(((otif_year[i] / transaksi_year[i]) * 100), 2))
    
    last_percent_otif = percent_otif_year[len(percent_otif_year) - 1]
    different_otif_year = round((percent_otif_year[len(percent_otif_year) - 1] - percent_otif_year[len(percent_otif_year) - 2]) ,2)

    cursor=connection.cursor()
    cursor.execute(rollup_category_otif)
    r5=dictfetchall(cursor)

    otif_category1 = []
    otif_category2 = []
    otif_category3 = []
    label_category = []
    label_tahun = []

    for i in range(len(r5)):
        if r5[i]['kategori'] != None:
            label_category.append(r5[i]['kategori'])

    for i in range(len(r5)):
        if r5[i]['tahun'] != None:
            if r5[i]['tahun'] not in label_tahun:
                label_tahun.append(r5[i]['tahun'])

    for i in range(len(r5)):
        if r5[i]['kategori'] == 'Furniture' :
            otif_category1.append(r5[i]['otif'])

    for i in range(len(r5)):
        if r5[i]['kategori'] == 'Office Supplies' :
            otif_category2.append(r5[i]['otif'])

    for i in range(len(r5)):
        if r5[i]['kategori'] == 'Technology' :
            otif_category3.append(r5[i]['otif'])   

    cursor=connection.cursor()
    cursor.execute(rollup_category_pengiriman)
    r6=dictfetchall(cursor)

    pengiriman_category1 = []
    pengiriman_category2 = []
    pengiriman_category3 = []
    
    for i in range(len(r6)):
        if r6[i]['kategori'] == 'Furniture' :
            pengiriman_category1.append(r6[i]['jumlah_pengiriman'])

    for i in range(len(r6)):
        if r6[i]['kategori'] == 'Office Supplies' :
            pengiriman_category2.append(r6[i]['jumlah_pengiriman'])

    for i in range(len(r6)):
        if r6[i]['kategori'] == 'Technology' :
            pengiriman_category3.append(r6[i]['jumlah_pengiriman'])  

    percent_otif_category1 = []
    percent_otif_category2 = []
    percent_otif_category3 = []

    for i in range(len(label_tahun)):
        percent_otif_category1.append(round(((otif_category1[i] /  pengiriman_category1[i]) * 100), 2))

    for i in range(len(label_tahun)):
        percent_otif_category2.append(round(((otif_category2[i] /  pengiriman_category2[i]) * 100), 2))

    for i in range(len(label_tahun)):
        percent_otif_category3.append(round(((otif_category3[i] /  pengiriman_category3[i]) * 100), 2))

    cursor=connection.cursor()
    cursor.execute(rollup_region_otif_per_year)
    r7=dictfetchall(cursor)

    otif_region1 = []
    otif_region2 = []
    otif_region3 = []
    label_region = []

    for i in range(len(r7)):
        if r7[i]['region'] != None:
            label_region.append(r7[i]['region'])

    for i in range(len(r7)):
        if r7[i]['region'] == 'Central' :
            otif_region1.append(r7[i]['otif'])

    for i in range(len(r7)):
        if r7[i]['region'] == 'North' :
            otif_region2.append(r7[i]['otif'])

    for i in range(len(r7)):
        if r7[i]['region'] == 'South' :
            otif_region3.append(r7[i]['otif'])   

    cursor=connection.cursor()
    cursor.execute(rollup_region_pengiriman)
    r8=dictfetchall(cursor)

    pengiriman_region1 = []
    pengiriman_region2 = []
    pengiriman_region3 = []
    
    for i in range(len(r8)):
        if r8[i]['region'] == 'Central' :
            pengiriman_region1.append(r8[i]['jumlah_pengiriman'])

    for i in range(len(r8)):
        if r8[i]['region'] == 'North' :
            pengiriman_region2.append(r8[i]['jumlah_pengiriman'])

    for i in range(len(r8)):
        if r8[i]['region'] == 'South' :
            pengiriman_region3.append(r8[i]['jumlah_pengiriman'])  

    percent_otif_region1 = []
    percent_otif_region2 = []
    percent_otif_region3 = []

    for i in range(len(label_tahun)):
        percent_otif_region1.append(round(((otif_region1[i] /  pengiriman_region1[i]) * 100), 2))

    for i in range(len(label_tahun)):
        percent_otif_region2.append(round(((otif_region2[i] /  pengiriman_region2[i]) * 100), 2))

    for i in range(len(label_tahun)):
        percent_otif_region3.append(round(((otif_region3[i] /  pengiriman_region3[i]) * 100), 2))

    content = {
        'last_on_time' : last_ontime,
        'last_in_full' : last_infull,
        'last_otif' : last_percent_otif,
        'last_transaksi' : last_transaksi,
        'beda_ontime' : different_ontime,
        'beda_infull' : different_infull,
        'beda_transaksi' : different_transaksi,
        'beda_persen_otif' : different_otif_year,
        'data_ontime' : ontime_year,
        'data_infull' : infull_year,
        'data_transaksi' : transaksi_year,
        'data_percent_otif' : percent_otif_year,
        'total_otif' : total_otif,
        'total_transaksi' : total_transaksi,
        'label_tahun' : label_tahun,
        'last_year' : last_year,
        'label_category' : label_category,
        'label_region' : label_region,
        'category1' : percent_otif_category1,
        'category2' : percent_otif_category2,
        'category3' : percent_otif_category3,
        'region1' : percent_otif_region1,
        'region2' : percent_otif_region2,
        'region3' : percent_otif_region3,
    }
    return render(request, 'logistic/logistic-yearly.html', content)

@login_required(login_url='login')
def yearly_logistic_2015(request):

    cursor=connection.cursor()
    cursor.execute(pivot_infull_month)
    r=dictfetchall(cursor)

    infull_2015 = []
    label_bulan = []
    sum_infull_2015 = 0
    for i in range(len(r)):
        if r[i]['tahun'] == '2015':
            for key, value in r[i].items():
                if key != 'tahun':
                    infull_2015.append(value)
                    label_bulan.append(key.capitalize())
                    sum_infull_2015 += value
                    

    cursor.execute(pivot_ontime_month)
    r2=dictfetchall(cursor)

    ontime_2015 = []
    sum_ontime_2015 = 0
    for i in range(len(r2)):
        if r2[i]['tahun'] == '2015':
            for key, value in r2[i].items():
                if key != 'tahun':
                    ontime_2015.append(value)
                    sum_ontime_2015 += value

    cursor.execute(pivot_otif_month)
    r3=dictfetchall(cursor)

    otif_2015 = []
    sum_otif_2015 = 0

    for i in range(len(r3)):
        if r3[i]['tahun'] == '2015':
            for key, value in r3[i].items():
                if key != 'tahun':
                    otif_2015.append(value)
                    sum_otif_2015 += value

    cursor.execute(pivot_pengiriman_month)
    r4=dictfetchall(cursor)

    pengiriman_2015 = []
    sum_pengiriman_2015 = 0

    for i in range(len(r4)):
        if r4[i]['tahun'] == '2015':
            for key, value in r4[i].items():
                if key != 'tahun':
                    pengiriman_2015.append(value)
                    sum_pengiriman_2015 += value

    percent_otif_2015 = []
    for i in range(len(pengiriman_2015)):
        percent_otif_2015.append(round(((otif_2015[i] / pengiriman_2015[i]) * 100), 2))

    sum_percent_otif_2015 = round(((sum_otif_2015 / sum_pengiriman_2015)*100), 2)

    content = {
        'label_bulan' : label_bulan,
        'infull' : infull_2015,
        'ontime' : ontime_2015,
        'otif' : otif_2015,
        'pengiriman' : pengiriman_2015,
        'percentage_otif' : percent_otif_2015,
        'sum_infull' : sum_infull_2015,
        'sum_ontime' : sum_ontime_2015,
        'sum_pengiriman' : sum_pengiriman_2015,
        'sum_percent' : sum_percent_otif_2015
    }

    return render(request, 'logistic/yearly/logistic-yearly-2015.html', content)

@login_required(login_url='login')
def yearly_logistic_2016(request):
    
    cursor=connection.cursor()
    cursor.execute(pivot_infull_month)
    r=dictfetchall(cursor)

    infull_2016 = []
    label_bulan = []
    sum_infull_2016 = 0
    for i in range(len(r)):
        if r[i]['tahun'] == '2016':
            for key, value in r[i].items():
                if key != 'tahun':
                    infull_2016.append(value)
                    label_bulan.append(key.capitalize())
                    sum_infull_2016 += value
                    

    cursor.execute(pivot_ontime_month)
    r2=dictfetchall(cursor)

    ontime_2016 = []
    sum_ontime_2016 = 0
    for i in range(len(r2)):
        if r2[i]['tahun'] == '2016':
            for key, value in r2[i].items():
                if key != 'tahun':
                    ontime_2016.append(value)
                    sum_ontime_2016 += value

    cursor.execute(pivot_otif_month)
    r3=dictfetchall(cursor)

    otif_2016 = []
    sum_otif_2016 = 0

    for i in range(len(r3)):
        if r3[i]['tahun'] == '2016':
            for key, value in r3[i].items():
                if key != 'tahun':
                    otif_2016.append(value)
                    sum_otif_2016 += value

    cursor.execute(pivot_pengiriman_month)
    r4=dictfetchall(cursor)

    pengiriman_2016 = []
    sum_pengiriman_2016 = 0

    for i in range(len(r4)):
        if r4[i]['tahun'] == '2016':
            for key, value in r4[i].items():
                if key != 'tahun':
                    pengiriman_2016.append(value)
                    sum_pengiriman_2016 += value

    percent_otif_2016 = []
    for i in range(len(pengiriman_2016)):
        percent_otif_2016.append(round(((otif_2016[i] / pengiriman_2016[i]) * 100), 2))

    sum_percent_otif_2016 = round(((sum_otif_2016 / sum_pengiriman_2016)*100), 2)

    content = {
        'label_bulan' : label_bulan,
        'infull' : infull_2016,
        'ontime' : ontime_2016,
        'otif' : otif_2016,
        'pengiriman' : pengiriman_2016,
        'percentage_otif' : percent_otif_2016,
        'sum_infull' : sum_infull_2016,
        'sum_ontime' : sum_ontime_2016,
        'sum_pengiriman' : sum_pengiriman_2016,
        'sum_percent' : sum_percent_otif_2016
    }

    return render(request, 'logistic/yearly/logistic-yearly-2016.html', content)

@login_required(login_url='login')
def yearly_logistic_2017(request):
    
    cursor=connection.cursor()
    cursor.execute(pivot_infull_month)
    r=dictfetchall(cursor)

    infull_2017 = []
    label_bulan = []
    sum_infull_2017 = 0
    for i in range(len(r)):
        if r[i]['tahun'] == '2017':
            for key, value in r[i].items():
                if key != 'tahun':
                    infull_2017.append(value)
                    label_bulan.append(key.capitalize())
                    sum_infull_2017 += value
                    

    cursor.execute(pivot_ontime_month)
    r2=dictfetchall(cursor)

    ontime_2017 = []
    sum_ontime_2017 = 0
    for i in range(len(r2)):
        if r2[i]['tahun'] == '2017':
            for key, value in r2[i].items():
                if key != 'tahun':
                    ontime_2017.append(value)
                    sum_ontime_2017 += value

    cursor.execute(pivot_otif_month)
    r3=dictfetchall(cursor)

    otif_2017 = []
    sum_otif_2017 = 0

    for i in range(len(r3)):
        if r3[i]['tahun'] == '2017':
            for key, value in r3[i].items():
                if key != 'tahun':
                    otif_2017.append(value)
                    sum_otif_2017 += value

    cursor.execute(pivot_pengiriman_month)
    r4=dictfetchall(cursor)

    pengiriman_2017 = []
    sum_pengiriman_2017 = 0

    for i in range(len(r4)):
        if r4[i]['tahun'] == '2017':
            for key, value in r4[i].items():
                if key != 'tahun':
                    pengiriman_2017.append(value)
                    sum_pengiriman_2017 += value

    percent_otif_2017 = []
    for i in range(len(pengiriman_2017)):
        percent_otif_2017.append(round(((otif_2017[i] / pengiriman_2017[i]) * 100), 2))

    sum_percent_otif_2017 = round(((sum_otif_2017 / sum_pengiriman_2017)*100), 2)

    content = {
        'label_bulan' : label_bulan,
        'infull' : infull_2017,
        'ontime' : ontime_2017,
        'otif' : otif_2017,
        'pengiriman' : pengiriman_2017,
        'percentage_otif' : percent_otif_2017,
        'sum_infull' : sum_infull_2017,
        'sum_ontime' : sum_ontime_2017,
        'sum_pengiriman' : sum_pengiriman_2017,
        'sum_percent' : sum_percent_otif_2017
    }

    return render(request, 'logistic/yearly/logistic-yearly-2017.html', content)

@login_required(login_url='login')
def yearly_logistic_2018(request):
    
    cursor=connection.cursor()
    cursor.execute(pivot_infull_month)
    r=dictfetchall(cursor)

    infull_2018 = []
    label_bulan = []
    sum_infull_2018 = 0
    for i in range(len(r)):
        if r[i]['tahun'] == '2018':
            for key, value in r[i].items():
                if key != 'tahun':
                    infull_2018.append(value)
                    label_bulan.append(key.capitalize())
                    sum_infull_2018 += value
                    

    cursor.execute(pivot_ontime_month)
    r2=dictfetchall(cursor)

    ontime_2018 = []
    sum_ontime_2018 = 0
    for i in range(len(r2)):
        if r2[i]['tahun'] == '2018':
            for key, value in r2[i].items():
                if key != 'tahun':
                    ontime_2018.append(value)
                    sum_ontime_2018 += value

    cursor.execute(pivot_otif_month)
    r3=dictfetchall(cursor)

    otif_2018 = []
    sum_otif_2018 = 0

    for i in range(len(r3)):
        if r3[i]['tahun'] == '2018':
            for key, value in r3[i].items():
                if key != 'tahun':
                    otif_2018.append(value)
                    sum_otif_2018 += value

    cursor.execute(pivot_pengiriman_month)
    r4=dictfetchall(cursor)

    pengiriman_2018 = []
    sum_pengiriman_2018 = 0

    for i in range(len(r4)):
        if r4[i]['tahun'] == '2018':
            for key, value in r4[i].items():
                if key != 'tahun':
                    pengiriman_2018.append(value)
                    sum_pengiriman_2018 += value

    percent_otif_2018 = []
    for i in range(len(pengiriman_2018)):
        percent_otif_2018.append(round(((otif_2018[i] / pengiriman_2018[i]) * 100), 2))

    sum_percent_otif_2018 = round(((sum_otif_2018 / sum_pengiriman_2018)*100), 2)

    content = {
        'label_bulan' : label_bulan,
        'infull' : infull_2018,
        'ontime' : ontime_2018,
        'otif' : otif_2018,
        'pengiriman' : pengiriman_2018,
        'percentage_otif' : percent_otif_2018,
        'sum_infull' : sum_infull_2018,
        'sum_ontime' : sum_ontime_2018,
        'sum_pengiriman' : sum_pengiriman_2018,
        'sum_percent' : sum_percent_otif_2018
    }

    return render(request, 'logistic/yearly/logistic-yearly-2018.html', content)

@login_required(login_url='login')
def quarterly_logistic(request):
    
    cursor=connection.cursor()
    cursor.execute(pivot_ontime_quarter)
    r=dictfetchall(cursor)

    ontime_quarter_2015 = []
    ontime_quarter_2016 = []
    ontime_quarter_2017 = []
    ontime_quarter_2018 = []
    label_tahun = []
    label_quarter = []

    for i in range(len(r)):
        if r[i]['tahun'] == '2015':
            for key, value in r[i].items():
                if key != 'tahun':
                    ontime_quarter_2015.append(value)
                    label_quarter.append(key.replace("_", " ").capitalize())
        elif r[i]['tahun'] == '2016' :
            for key, value in r[i].items():
                if key != 'tahun':
                    ontime_quarter_2016.append(value)       
        elif r[i]['tahun'] == '2017' :
            for key, value in r[i].items():
                if key != 'tahun':
                    ontime_quarter_2017.append(value)  
        elif r[i]['tahun'] == '2018' :
            for key, value in r[i].items():
                if key != 'tahun':
                    ontime_quarter_2018.append(value) 

    for i in range(len(r)):
        if r[i]['tahun'] != None :
            if r[i]['tahun'] not in label_tahun:
                label_tahun.append(r[i]['tahun'])

    total_ontime_quarter = ontime_quarter_2015 + ontime_quarter_2016 + ontime_quarter_2017 + ontime_quarter_2018
    last_ontime_quarter = total_ontime_quarter[len(total_ontime_quarter) - 1]
    different_ontime_quarter = (total_ontime_quarter[len(total_ontime_quarter) - 1] - total_ontime_quarter[len(total_ontime_quarter) - 2])

    cursor.execute(pivot_infull_quarter)
    r2=dictfetchall(cursor)

    infull_quarter_2015 = []
    infull_quarter_2016 = []
    infull_quarter_2017 = []
    infull_quarter_2018 = []

    for i in range(len(r2)):
        if r2[i]['tahun'] == '2015':
            for key, value in r2[i].items():
                if key != 'tahun':
                    infull_quarter_2015.append(value)
        elif r2[i]['tahun'] == '2016' :
            for key, value in r2[i].items():
                if key != 'tahun':
                    infull_quarter_2016.append(value)       
        elif r2[i]['tahun'] == '2017' :
            for key, value in r2[i].items():
                if key != 'tahun':
                    infull_quarter_2017.append(value)  
        elif r2[i]['tahun'] == '2018' :
            for key, value in r2[i].items():
                if key != 'tahun':
                    infull_quarter_2018.append(value)  

    total_infull_quarter = infull_quarter_2015 + infull_quarter_2016 + infull_quarter_2017 + infull_quarter_2018
    last_infull_quarter = total_infull_quarter[len(total_infull_quarter) - 1]
    different_infull_quarter = (total_infull_quarter[len(total_infull_quarter) - 1] - total_infull_quarter[len(total_infull_quarter) - 2])
    
    cursor.execute(pivot_otif_quarter)
    r3=dictfetchall(cursor)

    otif_quarter_2015 = []
    otif_quarter_2016 = []
    otif_quarter_2017 = []
    otif_quarter_2018 = []

    for i in range(len(r3)):
        if r3[i]['tahun'] == '2015':
            for key, value in r3[i].items():
                if key != 'tahun':
                    otif_quarter_2015.append(value)
        elif r3[i]['tahun'] == '2016' :
            for key, value in r3[i].items():
                if key != 'tahun':
                    otif_quarter_2016.append(value)       
        elif r3[i]['tahun'] == '2017' :
            for key, value in r3[i].items():
                if key != 'tahun':
                    otif_quarter_2017.append(value)  
        elif r3[i]['tahun'] == '2018' :
            for key, value in r3[i].items():
                if key != 'tahun':
                    otif_quarter_2018.append(value) 

    
    cursor.execute(pivot_pengiriman_quarter)
    r4=dictfetchall(cursor)

    pengiriman_quarter_2015 = []
    pengiriman_quarter_2016 = []
    pengiriman_quarter_2017 = []
    pengiriman_quarter_2018 = []
    

    for i in range(len(r4)):
        if r4[i]['tahun'] == '2015':
            for key, value in r4[i].items():
                if key != 'tahun':
                    pengiriman_quarter_2015.append(value)
        elif r4[i]['tahun'] == '2016' :
            for key, value in r4[i].items():
                if key != 'tahun':
                    pengiriman_quarter_2016.append(value)       
        elif r4[i]['tahun'] == '2017' :
            for key, value in r4[i].items():
                if key != 'tahun':
                    pengiriman_quarter_2017.append(value)  
        elif r4[i]['tahun'] == '2018' :
            for key, value in r4[i].items():
                if key != 'tahun':
                    pengiriman_quarter_2018.append(value)

    total_pengiriman_quarter = pengiriman_quarter_2015 + pengiriman_quarter_2016 + pengiriman_quarter_2017 + pengiriman_quarter_2018
    last_pengiriman_quarter = total_pengiriman_quarter[len(total_pengiriman_quarter) - 1]
    different_pengiriman_quarter = (total_pengiriman_quarter[len(total_pengiriman_quarter) - 1] - total_pengiriman_quarter[len(total_pengiriman_quarter) - 2])

    kpi_otif_2015 = []
    kpi_otif_2016 = []
    kpi_otif_2017 = []
    kpi_otif_2018 = []

    for i in range(len(otif_quarter_2015)):
        kpi_otif_2015.append(round(((otif_quarter_2015[i] / pengiriman_quarter_2015[i])*100), 3))        
    for i in range(len(otif_quarter_2016)):
        kpi_otif_2016.append(round(((otif_quarter_2016[i] / pengiriman_quarter_2016[i])*100), 3))
    for i in range(len(otif_quarter_2017)):
        kpi_otif_2017.append(round(((otif_quarter_2017[i] / pengiriman_quarter_2017[i])*100), 3))        
    for i in range(len(otif_quarter_2018)):
        kpi_otif_2018.append(round(((otif_quarter_2018[i] / pengiriman_quarter_2018[i])*100), 3))

    kpi_otif_quarter = kpi_otif_2015 + kpi_otif_2016 + kpi_otif_2017 + kpi_otif_2018
    last_otif_quarter = kpi_otif_quarter[len(kpi_otif_quarter) - 1]
    different_otif_quarter = round((kpi_otif_quarter[len(kpi_otif_quarter) - 1] - kpi_otif_quarter[len(kpi_otif_quarter) - 2]), 2)


    content = {
        'label_tahun' : label_tahun,
        'label_quarter' : label_quarter,
        'data_ontime_quarter' : total_ontime_quarter,
        'ontime_quarter' : last_ontime_quarter,
        'different_ontime' : different_ontime_quarter,
        'ontime_2015' : ontime_quarter_2015,
        'ontime_2016' : ontime_quarter_2016,
        'ontime_2017' : ontime_quarter_2017,
        'ontime_2018' : ontime_quarter_2018,
        'data_infull_quarter' : total_infull_quarter,
        'infull_quarter' : last_infull_quarter,
        'different_infull' : different_infull_quarter,
        'infull_2015' : infull_quarter_2015,
        'infull_2016' : infull_quarter_2016,
        'infull_2017' : infull_quarter_2017,
        'infull_2018' : infull_quarter_2018,
        'pengiriman_quarter' : last_pengiriman_quarter,
        'different_pengiriman' : different_pengiriman_quarter,
        'otif_2015' : kpi_otif_2015, 
        'otif_2016' : kpi_otif_2016,
        'otif_2017' : kpi_otif_2017,
        'otif_2018' : kpi_otif_2018,
        'otif_quarter' : last_otif_quarter,
        'different_otif' : different_otif_quarter,
    }

    return render(request, 'logistic/logistic-quarter.html', content)
