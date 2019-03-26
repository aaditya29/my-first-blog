##A view is a plave where we put the "logic" of our application.
#A view is a place where we put the "logic" of our application.
#It will request information from the model we created before and pass it to a template.

from django.shortcuts import render
from django.utils import timezone
from .models import Post#The . means current directory or current application

# Create your views here.
def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html', {})

#Here we greated a function called post_list that takes request and will return the value
#it gets from calling another function render that will render(put together our template)
