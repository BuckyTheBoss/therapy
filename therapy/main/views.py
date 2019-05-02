from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.core.mail import send_mail
from therapy.middleware.login_exempt import login_exempt
from .models import Therapist, Patient
from .forms import *


def profile_edit(request,id):
	if not request.user.is_patient:
		return redirect('doctor_profile_edit')
	patient = Patient.objects.filter(id=id).first()
	form = PatientForm(instance=patient)
	form2 = UserForm(instance=patient.user)
	if request.method == "POST":
		print(request.POST)
		form = PatientForm(request.POST, instance=patient)
		form2 = UserForm(request.POST, instance=patient.user)
		if form.is_valid() and form2.is_valid():
			form.save()
			form2.save()
	return render(request, 'profile_edit.html', {'patient' : patient, 'form' : form, 'form2' : form2} )
	

def doctor_profile_edit(request):
	return render(request, 'doctor_profile_edit.html')

def doctor_profile(request,id):
	therapist = Therapist.objects.filter(id=id).first()
	'''this will have the initial chat space display this as a card'''
	return render(request, 'doctor_profile.html', {'therapist' : therapist})

def doctor_index(request):
	'''this will have the initial chat space'''
	chats = Chat.objects.filter(therapist=request.user.therapist)
	return render(request, 'doctor_index.html', {'chats' : chats})

def index(request):
	if not request.user.is_patient:
		return redirect('doctor_index')
	therapists = Therapist.objects.filter(categories__in=request.user.patient.categories.all()).all()
	return render(request, 'index.html',{'therapists' : therapists})

@login_exempt
def signup(request):
	if request.method == 'POST':
		form = CustomUserCreationForm(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			user.is_patient=True
			user.save()
			'''hashing process here to give link'''
			send_mail('Congratulations on signing up to theratinder', 'Congrats on the signup!','theratinder@gmail.com',[user.email],fail_silently=False)
			return redirect('index') #should redirect to dead end page until user confirms email
	form = CustomUserCreationForm()
	return render(request, 'registration/signup.html', {'form' : form})


def patient_matched_index(request):
	
	return render(request, 'patient_matched_index.html')

@login_exempt
def front(request):
	if request.user.is_authenticated:
		return redirect('index')
	return render(request, 'front.html')

def patient_chat(request, therapist_id):
	therapist = Therapist.objects.filter(pk=therapist_id).first()
	chat = Chat.objects.filter(therapist__id=therapist_id).filter(patient__id=request.user.patient.id).first()
	unread_msg_ids = []
	unread_messages = Message.objects.filter(chat=chat,read=False, user=therapist.user)
	for message in unread_messages:
		unread_msg_ids.append(message.id)	
	unread_messages.update(read=True)

	if request.user.is_patient and chat == None:
		chat = Chat(therapist=Therapist.objects.get(pk=therapist_id), patient=request.user.patient)
		chat.save()
	if request.method == 'POST':
		message = Message(chat=chat, content=request.POST.get('content'), user=request.user)
		message.save()
	return render(request, 'chat.html', {'chat' : chat, 'unread_msg_ids' : unread_msg_ids})


@login_exempt
def about(request):
	return render(request, 'about.html')




def therapist_chat(request, chat_id):
	chat = Chat.objects.filter(pk=chat_id).first()
	unread_messages = Message.objects.filter(chat=chat,read=False, user=chat.patient.user)
	if chat.therapist != request.user.therapist:
		#flash message "not your chat to see"
		return redirect('index')

	if request.method == 'POST':
		message = Message(chat=chat, content=request.POST.get('content'), user=request.user)
		message.save()
	unread_messages.update(read=True)
	return render(request, 'therapist_chat.html', {'chat' : chat})


def all_therapist_chats(request, therapist_id):
	chats = Chat.objects.filter(therapist__id=therapist_id).all()
	return render(request, 'doc_chats.html', {'chats' : chats})




