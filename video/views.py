from django.http import Http404
from django.shortcuts import render, get_object_or_404

from .models import Category, Video, Author


def search(request):
    param = request.GET.get('search', "")

    videos = Video.objects.filter(name__icontains=param)

    return render(request, "busca.html", {"param": param, "results": videos})


def videos(request):
    categories_list = Category.objects.all()
    return render(request, "categorias.html", {"categories": categories_list})


def category_view(request, slug):
    category = get_object_or_404(Category, slug=slug)
    videos = Video.objects.filter(category=category)

    return render(request, "categoria.html", {"category": category,
                                              "videos": videos})


def author_view(request, slug):
    author = get_object_or_404(Author, slug=slug)
    videos = Video.objects.filter(authors=author)

    return render(request, "author.html", {"author": author,
                                           "videos": videos})
