from django.shortcuts import render

from .models import Therapist , Patient


from .models import Therapist

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView
from .forms import *
from django.core.mail import send_mail


# Create your views here.
def profile_edit(request,id):
	patient = Patient.objects.filter(id=id).first()
	form = PatientForm(instance=patient)
	form2 = UserForm(instance=patient.user)
	return render(request, 'profile_edit.html' ,{'patient' : patient, 'form' : form, 'form2' : form2})

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


def patient_chat(request, therapist_id):
	chat = Chat.objects.filter(therapist__id=therapist_id).filter(patient__id=request.user.patient.id).first()
	if request.user.is_patient and chat == None:
		chat = Chat(therapist=Therapist.objects.get(pk=therapist_id), patient=request.user.patient)
		chat.save()
	if request.method == 'POST':
		message = Message(chat=chat, content=request.POST.get('content'), user=request.user)
		message.save()
	return render(request, 'chat.html', {'chat' : chat})


# def therapist_chat(request, chat_id)
# 	chat = Chat.objects.filter(pk=chat_id)
# 	if chat.therapist != request.user.therapist:
# 		#flash message "not your caht to see"
# 		return redirect('index')


