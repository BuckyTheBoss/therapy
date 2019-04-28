from django.contrib.auth.models import AbstractUser
from django.db import models
from .models import *

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ('category', 'gender', 'birthdate', 'bio')
        
class TherapistForm(forms.ModelForm):
    class Meta:
        model = Therapist
        fields = ('address', 'experience', 'education', 'languages', 'category', 'gender', 'birthdate', 'bio')