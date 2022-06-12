from django.shortcuts import render, redirect, get_object_or_404, HttpResponse 
from django.db.models import Q 
from django.core.paginator import Paginator
from .models import * 


# Create your views here.
def post_list_view(request):
    post_data = Post.objects.all()
    catg_data = Category.objects.all()

    page = request.GET.get('page', 1)
    paginator = Paginator(post_data, 10)
    post_data = paginator.get_page(page)

    context = {
        'title':'Posts List',
        'post_data':post_data,
        'catg_data':catg_data,
    }
    return render(request, 'posts/post_list.html', context)


def post_detail_view(request, ids):
    post_ids = get_object_or_404(Post, id=ids)
    context = {
        'title':'Post Details',
        'post_ids':post_ids,
    }
    return render(request, 'posts/post_detail.html', context)


def catg_detail_view(request, ids):
    catg_data = Category.objects.all()

    catg_ids = get_object_or_404(Category, id=ids)
    post_data = Post.objects.filter(category=catg_ids)

    page = request.GET.get('page', 1)
    paginator = Paginator(post_data, 10)
    post_data = paginator.get_page(page)

    context = {
        'title':'Category Details',
        'post_data':post_data,
        'catg_data':catg_data,
    }
    return render(request, 'posts/post_list.html', context)


def search_post_view(request): 
    catg_data = Category.objects.all()

    query = request.GET.get('q', None)
    if query == None or query == "":
        post_data = Post.objects.all()
    elif query is not None:
        post_data = Post.objects.filter(
            Q(category__title__icontains=query)|
            Q(title__icontains=query)|
            Q(content__icontains=query)|
            Q(date__icontains=query)
        ).distinct()

    context = {
        'title':'Search Post',
        'post_data':post_data,
        'catg_data':catg_data,
    }
    return render(request, 'posts/post_list.html', context)




