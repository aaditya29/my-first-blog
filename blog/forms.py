"""
With forms we will have absloyte power over our interface
"""
from django import forms
from .models import Post

class PostForm(forms, ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'text',)