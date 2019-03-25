from django.conf import settings
from django.utils import timezone
from django.db import models

# Create your models here.
class Post(models.Model):#models.Model means that the Post is a Django Model, so Django knows that it should be saved in the database
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)#Link to another model
    title = models.CharField(max_length=200)#This is how we define text with a limited number of characters
    text = models.TextField()#This is for long text without a limit
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank = True, null = True)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

