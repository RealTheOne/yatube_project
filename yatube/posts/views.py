from django.shortcuts import render
#from django.http import HttpResponse 

# Create your views here.

def index(request):
    template = 'posts/index.html'
    main_header = 'Это главная страница проекта Yatube'
    context = {
        'header': main_header
    }
    return render(request, template, context)

def group_posts(request, slug):
    template = 'posts/group_list.html'
    main_header = 'Здесь будет информация о группах проекта Yatube'
    context = {
        'header': main_header
    }
    return render(request, template, context)
