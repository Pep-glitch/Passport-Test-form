from django.shortcuts import render
from django.http import HttpResponse

def save_data(request):
    #send data to database
    return HttpResponse("whatever")


def show_page(request):
    #display the page
    return render(request,'no3.html')
# Create your views here.
