from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.core.mail import send_mail

from .models import Therapist, Patient
from .forms import *


def profile_edit(request,id):
	patient = Patient.objects.filter(id=id).first()
	form = PatientForm(instance=patient)
	form2 = UserForm(instance=patient.user)
	return render(request, 'profile_edit.html' ,{'patient' : patient, 'form' : form, 'form2' : form2})


	# def complete_patient_profile(request):
	# if request.method == 'POST':
	# 	form = PatientForm(request.POST)
	# 	if form.is_valid():
	# 		patient.save()

	# form = PatientForm()
	# return render(request, 'profile_edit.html', {'form' : form})

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
	therapists = Therapist.objects.all()
	'''queeris here button to redrect to 
	patient_matched_index when you have started an interaction with acouncilor
	 after a chat this will show up in the navbar if logged in and have assined councilor'''

	return render(request, 'index.html',{'therapists' : therapists})


def signup(request):
	if request.method == 'POST':
		form = CustomUserCreationForm(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			user.is_patient=True
			user.save()
			'''hashing process here to give link'''
			send_mail('Congratulations on signing up to theratinder', 'Click the confirmation in order to login to your profile {}'.format('login'),'theratinder@gmail.com',[user.email],fail_silently=False)
			return redirect('index') #should redirect to dead end page until user confirms email
	form = CustomUserCreationForm()
	return render(request, 'registration/signup.html', {'form' : form})


def patient_matched_index(request):
	
	return render(request, 'patient_matched_index.html')
