from django.shortcuts import render
from .models import server_list
from django.db import connection, transaction
from django.http import HttpResponse
#import models

# Create your views here.

def serlist(request):
    cursor = connection.cursor()
    cursor.execute('select * from server_list')
    raw = cursor.fetchall()
    output = '\n'.join([dict(p) for p in raw])
    return HttpResponse(output)
    #return render(request, 'app/index.html')

def index(request):
    return render(request, 'app/index.html')
