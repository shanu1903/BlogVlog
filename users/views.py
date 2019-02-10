from django.shortcuts import render,redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from  django.contrib import messages
from .forms import UserRegisterForm , UserUpdateForm , ProfileUpdateForm
# Create your views here.

def register(request):
	if(request.method == "POST"):
		form = UserRegisterForm(request.POST)
		if(form.is_valid()):
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request , f'Account created for {username}!')
			return redirect('home')
	else:
		form = UserRegisterForm()
	return render(request ,'users/register.html' , { 'form' : form } )




@login_required
def profile(request):

	if request.method =='POST':
		p_form = ProfileUpdateForm(request.POST , request.FILES , instance  = request.user.profile)
		u_form = UserUpdateForm(request.POST , instance = request.user)

		if p_form.is_valid() and u_form.is_valid():
			p_form.save()
			u_form.save()
			messages.success(request , f'Your account has been updated!!')
			return redirect('profile')
	
	else:

		p_form = ProfileUpdateForm(instance = request.user.profile)
		u_form = UserUpdateForm(instance = request.user)

	content = {
		'p_form' : p_form,
		'u_form' : u_form
	}
	return render(request , 'users/profile.html' , content )