from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from crops.forms import *
from crops.models import *
import datetime
from time import time

import datetime
# Create your views here.

def index(request):
    search = ''
    crops = Crop.objects.all()

    if len(request.GET) >0:
        search = str(request.GET["crop_search"])
        crops = Crop.objects.filter(name__startswith = search)
        
        
        
    objs = {'crops' : crops,'search' : search}
    return render(request,'index.html',objs)
    
    
    
def admin(request):
     
     
     if len(request.GET)  > 0:
         
         r= request.GET
         
         c = r['crop']
         v = r['variety']
         d = r['district']
         s = r['state']
         m = r['market']
         c = Crop.objects.get(name = c)
         v = Variety. objects.get(name = v,crop = c)
         m = Market.objects.get(name = m,state = s, district = d)
         
         if len(Items.objects.filter(crop = c,variety = v,market = m,date = r['date'])) == 0:
             
             obj = Items.objects.create(crop = c,variety = v,market = m,date = r['date'],price = r['price'])
             obj.save()
             print('created : ',obj)
     crops = Crop.objects.all()
     forms = {'market_form' : MarketForm(),'crop_form' : CropForm(),'variety_form' : VarietyForm()}
     
     objs = {'crops' : crops,'forms' : forms}
     return render(request,'admin.html',objs)

     
def add_data(request,Type):
    if Type == 'market':
        f = MarketForm(request.GET)
    elif Type == 'crop':
        f = CropForm(request.POST,request.FILES)
    elif Type == 'variety':
        f = VarietyForm(request.GET)
    if f.is_valid():
            f.save()
    return redirect('/admin_pannel')
        
def details(request,crop):
    c = Crop.objects.get(name = crop)
    img_url = c.img.url
    items = Items.objects.filter(crop__name = crop)
    state = ''
    district = ''
    market = ''
    if len(request.GET) > 0:
        state = request.GET['state_search']
        district = request.GET['district_search']
        market = request.GET['market_search']
        m = Market.objects.filter(items__in = items,name__startswith = market,state__startswith = state,district__startswith = district).distinct()
    else:
        m = Market.objects.filter(items__in = items).distinct()
    objs = {'img' : img_url,'crop':crop,'markets':m,'filters':{'state':state,'district':district,'market':market}}
    return render(request,'details.html',objs)


def search_market(request):
    crop = request.GET['crop_search']
    print('crop : ',crop)
    return details(request,crop = crop)


def View(request,crop,market):
    From = str(datetime.date.today())
    To = str(datetime.date.today())
    if len(request.GET) > 0:
        From = request.GET['from']
        To = request.GET['to']
    items = Items.objects.filter(crop__name = crop,market__name = market,date__gte = From,date__lte = To)
    args = {'items' : items,'crop':crop,'market':market,'From':From,'To':To}
    return render(request,'view.html',args)



@csrf_exempt     
def test(request):
     req = eval(request.body.decode())
     req.setdefault('target','')
     r = []
     if req["target"] == 'variety':
         po = Variety.objects.filter(crop__name =  req["value"])
         for i in po.values():
             r.append(i['name'])
             
     elif req["target"] == 'state':
         po = Market.objects.all()
         for i in po.values():
             r.append(i['state'])
     elif req["target"] == 'district':
         po = Market.objects.filter(state = req["value"])
         for i in po.values():
             r.append(i['district'])
     elif req["target"] == 'market':
         po = Market.objects.filter(district = req["value"])
         for i in po.values():
             r.append(i['name'])
     r = list(set(r))  
     
     res = '","'.join(list(map(str,r)))
     res = '["' + res+'"]'
     return HttpResponse(res)     
     