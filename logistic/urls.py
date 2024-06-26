from django.urls import path
from logistic.views import *

urlpatterns = [
    path('', index, name='logistic'),
    path('yearly-logistic', logistic_yearly, name='yearly-logistic'),
    path('yearly-logistic-2015', yearly_logistic_2015, name='yearly-logistic-2015'),
    path('yearly-logistic-2016', yearly_logistic_2016, name='yearly-logistic-2016'),
    path('yearly-logistic-2017', yearly_logistic_2017, name='yearly-logistic-2017'),
    path('yearly-logistic-2018', yearly_logistic_2018, name='yearly-logistic-2018'),
    path('quarterly-logistic', quarterly_logistic, name='quarterly-logistic'),
]