from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    query = request.GET.get('name')
    message = "Hey {} i can change u !".format(query)
    template = "home.html"
    context = {
        'message':message,
    }
    return render(request, template, context)
