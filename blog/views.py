##A view is a plave where we put the "logic" of our application.
#A view is a place where we put the "logic" of our application.
#It will request information from the model we created before and pass it to a template.

from django.shortcuts import render
from django.shortcuts import redirect
from django.utils import timezone
from .forms import PostForm
from django.shortcuts import render, get_object_or_404
from .models import Post#The . means current directory or current application

# Create your views here.
def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html', {})

def post_detail(request,pk):
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

#Here we greated a function called post_list that takes request and will return the value
#it gets from calling another function render that will render(put together our template)
