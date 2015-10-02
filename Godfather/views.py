import json
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext, loader
from django.contrib.auth import authenticate
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.models import UserManager
from django.contrib.auth.hashers import (
	check_password, is_password_usable, make_password,
)
from django.contrib.auth.decorators import login_required

# from .forms import SignupForm


from .models import MyUser, Location, Article

def home(request):
	message  = "Welcome to C.O.G Talk"
	# u_message = "your actuality"

	if request.method == 'POST':
		username = request.POST.get('username', '')
		password = request.POST.get('password', '')
		user = auth.authenticate(username=username , password=password)

		if user is not None:
			auth.login(request, user)
			return HttpResponse('/account/')
		else:
			return HttpResponse('Your account had been desactivated')
	else:
	# c = {}
	# c.update(csrf(request))
		template = loader.get_template('home.html')
		context = RequestContext(request, {
			'message':message,
			# 'u_message':u_message
				# c,
			})

		return HttpResponse(template.render(context))

def login(request):
	message = "Welcome back to C.O.G Talk"
	u_message = "You are logged in "

	if request.method == 'POST':
		username = request.POST.get('username', '')
		password = request.POST.get('password', '')
		user = auth.authenticate(username=username , password=password)

		if user is not None:
			auth.login(request, user)
			return HttpResponseRedirect('/accounts/')
		else:
			return HttpResponse('Your account had been desactivated')
	else:
		template = loader.get_template('login.html')
		context = RequestContext(request, {
			   'message':message,
			   'u_message':u_message
					# c,
				})

		return HttpResponse(template.render(context))

@login_required
def profile(request):
	message = ""
	template = loader.get_template('profile.html')
	context = RequestContext(request, {
				'message':message
			})

	return HttpResponse(template.render(context))

def logout(request):
	message = "Successfully logged out"
	auth.logout(request)
	template = loader.get_template('logout.html')
	context = RequestContext(request, {
				# c,
				'message':message
			})

	return HttpResponse(template.render(context))

def register(request):
	message = 'Please register !'
	if request.method == 'POST':
		username = request.POST.get('username', '')
		lastname = request.POST.get('lastname', '')
		firstname = request.POST.get('firstname', '')
		password1 = request.POST.get('password1', '')
		password2 = request.POST.get('password2', '')
		email = request.POST.get('email', '')
		
		if password1 != password2:
			raise ValueError('Passwords dont match')
		else:
			user = MyUser.objects.create(
			username = username,
			password= make_password(password2),
				first_name = firstname,
				last_name = lastname,
				email = email
			  )

			if user is not None:
				return HttpResponseRedirect('/account/register_success/')
			else:
				return HttpResponseRedirect('Failed to Register !')
		

	template = loader.get_template('register.html')
	context = RequestContext(request, {
		   'message':message
	})


	return HttpResponse(template.render(context))

def register_success(request):
	message = " You have registered successfully ! Please click on link below to log into your account !"
	template = loader.get_template('register_success.html')
	context = RequestContext(request, {
		'message':message
	})

	return HttpResponse(template.render(context))

def news(request):
	message = 'Breaking news'
	template = loader.get_template('news.html')
	context = RequestContext(request, {
				# c,
				'message':message
			})

	return HttpResponse(template.render(context))

def talents(request):
	template = loader.get_template('talents.html')
	context = RequestContext(request, {

		})
	return HttpResponse(template.render(context))

@login_required
def talk(request):
	template = loader.get_template('social.html')
	context = RequestContext(request, {

		})
	return HttpResponse(template.render(context))

def about(request):
	template = loader.get_template('about.html')
	context = RequestContext(request, {

		})
	return HttpResponse(template.render(context))