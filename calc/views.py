
from django.shortcuts import render
from django.http import HttpResponse
from .models import get_all_data
# Create your views here.

data = get_all_data()

def home(request):
    query = request.GET.get('name')
    message = "Hey {} i can change u !".format(query)
    template = "home.html"
    context = {
        'data': data,
    }
    return render(request, template, context)
