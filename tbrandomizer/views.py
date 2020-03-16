"""View functions for Tbrandomizer"""
from django.shortcuts import render

def index(request):
    """Returns main tbrandomizer view"""
    return render(request, 'tbrandomizer/index.html')
