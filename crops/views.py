from . models import *
import os,sys
from django.shortcuts import render
import pandas as pd
# Create your views h


def load(request):
    path = 'C:/Users/Dhananjay P/django/agri/datasets/'
    files = os.listdir(path)[7:]
    for f in files:
        df = pd.read_csv(path+f)
        df.reindex(index=df.index[::-1])
        l = len(df)
        for i in df.iterrows():
            sys.stdout.write('\rprocessing : '+f+' '+str(round((i[0]/l)*100,2))+'%')
            i = i[1]
            p = i.arrival_date.replace('/','-')
            try:
                date = p[6:] + p[2:5] + '-'+p[:2]
                m,mc = Market.objects.get_or_create(state = i.state,district = i.district,name = i.market.replace('/',' or '))
                c,cc = Crop.objects.get_or_create(name = i.commodity.replace('/',' or '))
                v,vc = Variety.objects.get_or_create(crop = c,name = i.variety.replace('/',' or '))
                I,ic = Items.objects.get_or_create(crop = c,market = m,variety = v,date = date,min_price = float(i.min_price),max_price = float(i.max_price),mod_price = float(i.modal_price))
            except:
                pass