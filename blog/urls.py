from django.urls import path
from . import views#We're importing Django's function path and all of out
					#views from the blog application

urlpatterns = [
	path('', views.post_list, name = 'post_list'),
	]