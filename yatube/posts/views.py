from django.shortcuts import render, get_object_or_404
from .models import Post, Group

# Create your views here.
def index(request):
    posts = Post.objects.order_by('-pub_date')[:10]
    main_header = 'Это главная страница проекта Yatube'
    title = 'Последние обновления на сайте'
    context = {
        'posts': posts,
        'header': main_header,
        'title': title
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    main_header = 'Лев Толстой - зеркало русской революции.'
    title = 'Записи сообщества'
    context = {
        'title': title,
        'header': main_header,
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
