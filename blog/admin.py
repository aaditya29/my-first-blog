from django.contrib import admin
from .models import Post

admin.site.register(Post)#We import the Post model defined in the models.py. To make our model visible on the admin page, we need to register the model
# Register your models here.
