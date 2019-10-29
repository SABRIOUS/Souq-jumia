from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
# Create your views here.

def home(request):

    return render(request,'home.html')


def new_search(request):
    search = request.POST.get('search')
    context = {
        'search':search,
    }
    print(search)

    return render(request,'ecommerce_comparison/new_search.html',context)
