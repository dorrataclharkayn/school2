# Create your views here.
from decimal import Decimal
from datetime import date


from django.shortcuts import render
from .models import login11,matiere,nstudent101,student101,anne,regeleve,stok,stok11,visamoy,mony,school,ps123note,regeleveps,mediaschool,videoschool,newsschool
from django.template import loader
from .form02 import loginform
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from num2words import num2words

x=0
z1zmat=matiere.objects.all()

y=50000
#for i in range(y):
  #  print(y)
