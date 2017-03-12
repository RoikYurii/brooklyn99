from django.shortcuts import render, redirect
from .models import New
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def news_list(request):
    news_list = New.objects.order_by('-data_added')
    paginator = Paginator(news_list, 3)
    page = request.GET.get('page')
    try:
    	news = paginator.page(page)
    except PageNotAnInteger:
    	news = paginator.page(1)
    except EmptyPage:
    	news = paginator.page(paginator.num_pages)
    if page == '1':
    	return redirect ('main:index', permanent = True)
    context = {
        'news': news,
    }
    return render(request, 'main/index.html', context)

def new_detail(request, new_id):
    new = New.objects.get(id = new_id)
    context = {
        'new': new,
    }
    return render(request, 'main/new_detail.html', context)