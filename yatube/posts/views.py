#from django.shortcuts import render (ORIGINAL IMPORT. WHAT THE HELL IS THAT?!)
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('Главная страница. A small step for a...')

def group_posts(request, slug):
    return HttpResponse(f'Here should be something about "group posts" {slug}')
