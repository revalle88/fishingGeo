from django.shortcuts import render
from django.shortcuts import redirect
import json
# Create your views here.
from django.http import HttpResponse
from .models import Pound
from .forms import PoundForm


def index(request):
	pounds = Pound.objects.all()
	return render(request, 'index.html',  {"pounds": pounds})

 #   return HttpResponse("Hello, world. You're at the polls index.")

def pounds(request):
	pounds = Pound.objects.all()
	
	#pounds_for_js = json.dumps(pounds)
	return render(request, 'pounds.html',  {"pounds": pounds})

def pounds(request):
	pounds = Pound.objects.all()
	
	#pounds_for_js = json.dumps(pounds)
	return render(request, 'pounds.html',  {"pounds": pounds})




def pound_new(request):
    if request.method == "POST":
        form = PoundForm(request.POST)
        if form.is_valid():
            pound = form.save(commit=False)
            pound.save()
            return redirect('index')
    else:
    	form = PoundForm()
    return render(request, 'pound_edit.html', {'form': form})