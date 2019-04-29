
from django.shortcuts import render
from .models import Therapist

from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views.generic import CreateView



# Create your views here.
def profile_edit(request):
	return render(request, 'profile_edit.html')

def doctor_profile_edit(request):
	return render(request, 'doctor_profile_edit.html')

def doctor_profile(request):
	therapists = Therapist.objects.all()
	'''this will have the initial chat space display this as a card'''
	return render(request, 'doctor_profile.html', {'therapists' : therapists})

def doctor_index(request):
	'''this will have the initial chat space'''
	return render(request, 'doctor_index.html')

def index(request):
	return render(request, 'index.html')



