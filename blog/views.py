from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.utils import timezone
from .forms import PostForm, sum_form
from django.http import HttpResponseRedirect

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by
    ('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def get_result(request):
    if request.method == "POST":       
        answer = sum_form(request.POST)
        answer1 = sum_form()

     #   answer1.fields['edit_result'].label = ''
        
         

        a  = int (answer['edit1'].data) + int (answer['edit2'].data)
        answer1.fields['edit_result'].initial = a

        return render(request, 'blog/post_list.html',{'answer1': answer1})
           
    else:
        answer = sum_form()

    
    return render(request, 'blog/post_list.html',{'answer': answer})
		
