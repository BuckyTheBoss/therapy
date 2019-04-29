from django.shortcuts import render

from .models import Therapist , Patient


from .models import Therapist

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from django.core.mail import send_mail


# Create your views here.
def profile_edit(request,id):
	patients = Patient.objects.filter(id=id)
	send_mail('test title', 'test email for theratinder','theratinder@gmail.com',['ozkilim@hotmail.co.uk'],fail_silently=False)
	return render(request, 'profile_edit.html' ,{'patients' : patients})

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


def signup(request):
	if request.method == 'POST':
		form = CustomUserCreationForm(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			user.is_patient=True
			user.save()
			return redirect('index') #should redirect to dead end page until user confirms email
	form = CustomUserCreationForm()
	return render(request, 'registration/signup.html', {'form' : form})
