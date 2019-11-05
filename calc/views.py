from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("Hey Itzik ! I hope your hand will better soon ! ")
