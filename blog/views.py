from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.timezone import now

from .forms import PostForm
from .models import Post, Tag


def index(request):
    posts = Post.objects.all().order_by("-published_date")
    paginator = Paginator(posts, 10)

    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    is_paginated = page.has_other_pages()

    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''

    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''

    context = {
        'page_object': page,
        'is_paginated': is_paginated,
        'next_url': next_url,
        'prev_url': prev_url
    }

    return render(request, 'blog/index.html', context=context)


def post(request, id=None):
    post = get_object_or_404(Post, pk=id)
    return render(request, 'blog/post.html', context={"post": post})


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags.html', context={'tags': tags})


def tag_detail(request, slug):
    tag = get_object_or_404(Tag, slug__iexact=slug)
    return render(request, 'blog/tag_detail.html', context={'tag': tag})


@login_required
def create(request):
    error = ''
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.creation_date = now()
            post.editing_date = now()
            post.user = request.user
            post.save()
            return redirect('index')
        else:
            error = 'Форма была неверной'
    form = PostForm
    context = {
        'form': form,
        'error': error,
    }
    return render(request, "blog/create.html", context)

# To be continued...


# from django.db.models import Q
# from django.views.generic import UpdateView, DeleteView

# def search(request):
#     search_query = request.GET.get('query', '')
#     if search_query:
#         posts = Post.objects.filter(Q(title__icontaints=search_query) | Q(body__icontaints=search_query))
#     else:
#         posts = Post.objects.all()
#
#     return render(request, 'blog/index.html', context={'posts': posts})
#
#
# def update_(UpdateView):
#     model = Post
#     template_name = 'blog/update.html'
#     fields = ['title', 'content', 'editing_date', 'image', 'tags']
#
#
# def delete_(DeleteView):
#     model = Post
#     success_url = '/blog/'
#     template_name = 'blog/delete.html'
