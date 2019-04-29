from django.contrib.auth.models import AbstractUser
from django.forms import ModelForm
from .models import *
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm



class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = ('category', 'gender', 'birthdate', 'bio')
        

class TherapistForm(ModelForm):
    class Meta:
        model = Therapist
        fields = ('address', 'experience', 'education', 'languages', 'category', 'gender', 'birthdate', 'bio')


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email')