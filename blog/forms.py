from django import forms
from .models import posts


class CreatePost(forms.ModelForm):

	class Meta:
		model = posts
		fields =['title' , 'content']

	 