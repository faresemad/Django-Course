from django.shortcuts import redirect, render

from .forms import PostForm
from .models import Post

# Create your views here.


def home(request):
    context = {'posts': Post.objects.all()}
    return render(request, 'posts/home.html', context)
def post_details(request, id):
    context = {'post': Post.objects.get(id=id)}
    return render(request, 'posts/post_details.html', context)

def post_create(request):
    single = PostForm()
    if request.method == 'POST':
        single = PostForm(request.POST, request.FILES)
        if single.is_valid():
            single.save()
        return redirect('posts:home')
    else:
        single = PostForm()
    return render(request, 'posts/post_create.html', {'form': single})

def post_update(request,id):
    single = Post.objects.get(id=id)
    if request.method == 'POST':
        single = PostForm(request.POST, request.FILES,instance = single)
        if single.is_valid():
            single.save()
        return redirect('posts:home')
    else:
        single = PostForm(instance=single)
    return render(request, 'posts/post_update.html', {'form': single})
def post_delete(request,id):
    single = Post.objects.get(id=id)
    single.delete()
    return redirect('posts:home')

def about(request):
    return render(request, 'posts/about.html')


def contact(request):
    return render(request, 'posts/contact.html')