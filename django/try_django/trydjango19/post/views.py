from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from .models import Post
from .forms import PostForm


def post_create(request):
    form = PostForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        instance = form.save(commit=False)
        print(form.cleaned_data.get('title'))
        instance.save()
        messages.success(request, "Successfully created")
        return HttpResponseRedirect(instance.get_absolute_url())

    return render(request, 'create.html', {'form': form})


def post_detail(request, pk=None):
    # Usefull when a query might not fit the database
    obj = get_object_or_404(Post, pk=pk)

    context = {
        'title': 'detail',
        'post': obj,
    }
    return render(request, 'details.html', context)


def post_list(request):
    # CHeck if user is auth
    #    if request.user.is_authenticated()

    # Comment out is the ordering (now check the model meta class)
    queryset = Post.objects.all()  # order_by('-timestamp')
    context = {
        'post_list': queryset,
        'title': 'list',
    }
    return render(request, 'list.html', context)


def post_update(request, pk=None):
    # Usefull when a query might not fit the database
    instance = get_object_or_404(Post, pk=pk)
    form = PostForm(request.POST or None,
                    request.FILES or None, instance=instance)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Successfully saved", extra_tags='some-tag')
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        'title': instance.title,
        'post': instance,
        'form': form
    }
    return render(request, 'create.html', context)


def post_delete(request, pk=None):
    instance = get_object_or_404(Post, pk=pk)
    instance.delete()
    messages.success(request, 'Deleted')
    return redirect("post:list")
