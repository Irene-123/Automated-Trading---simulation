from django.http import HttpResponse
from django.shortcuts import render
import pandas as pd
import csv
from .forms import InputForm
from .forms import GeeksForm
import sys
# sys.path.append(r'C:\Users\kirti\Automated Trading_simulation\automatedTrader\back_end')
from automatedTrader.back_end.trader import trader

  
def index(request): 
    return  render(request, 'index.html')   

def ohlc(request): 
    csv_fp = open(f'static/ohlc.csv', 'r')
    reader = csv.DictReader(csv_fp)
    headers = [col for col in reader.fieldnames]
    out = [row for row in reader]
    return render(request, 'ohlc.html', {'data' : out, 'headers' : headers})
   
def ohlcform(request): 
    myform= InputForm() 
    return render(request, 'ohlcform.html', {'form': myform})

def formdata(request): 
    exchange, exchangeType, scripCode='', '', '' 
    if request.method=='GET': 
        form = InputForm(request.GET) 
        if form.is_valid(): 
            exchange= form.cleaned_data['exchange']
            exchangeType= form.cleaned_data['exchangeType']
            scripCode= form.cleaned_data['scripCode']
            # timeframe= form.cleaned_data['timeframe']
            # startdate= forms.cleaned_data['startdate']
            # enddate= forms.cleaned_data['enddate']
            print(exchange, exchangeType, scripCode) 
        else:
            raise Exception('Form not validated')
    csv_fp = open(f'static/ohlc.csv', 'r')
    reader = csv.DictReader(csv_fp)
    headers = [col for col in reader.fieldnames]
    out = [row for row in reader]
    return render(request, 'ohlc.html', {'data' : out, 'headers' : headers})

def socket_data(request): 
    file_path= open(f'static/socket_data.csv', 'r')
    reader= csv.DictReader(file_path) 
    headers= [col for col in reader.fieldnames] 
    out= [row for row in reader] 
    return render(request, 'socket_data.html', {'data': out, 'headers': headers} ) 




def trade(request): 
    context ={}
 
    # create object of form
    form = GeeksForm(request.POST or None, request.FILES or None)
     
    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        form.save()
 
    context['form']= form
    return render(request, "trade.html", context)





