from django.shortcuts import render
import json
# Create your views here.
from django.http import HttpResponse
from .models import Pound


def index(request):
	pounds = Pound.objects.all()
	return render(request, 'index.html',  {"pounds": pounds})

 #   return HttpResponse("Hello, world. You're at the polls index.")

def pounds(request):
	pounds = Pound.objects.all()
	
	#pounds_for_js = json.dumps(pounds)
	return render(request, 'pounds.html',  {"pounds": pounds})
