from django.urls import path
from . import views#We're importing Django's function path and all of out
					#views from the blog application

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]
#Here we assigning a view called post_list to the root URL. This URL pattern will
#match an empty string and the Django URL resolver will ignore the domain name the prefixes
#the full URL path

#The lart, name='post_list', is the name of the URL that will be used to identify the view.
"""
The post/<int:pk> specififes a URL pattern

post/ means that the URL should begin with the word post followed by a /
<int:pk> means that Django expects an int value and will transfer it to a view as a variable called pk.
/ it is sign again we need before finishing the URL
"""
