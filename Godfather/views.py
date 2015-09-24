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

# from .forms import SignupForm


from .models import MyUser, Location, Article

def home(request):
	message  = "Welcome to the C.O.G Talk"
	# c = {}
	# c.update(csrf(request))
	template = loader.get_template('home.html')
	context = RequestContext(request, {
		'message':message
			# c,
		})

	return HttpResponse(template.render(context))