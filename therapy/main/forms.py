from django import forms
from django.contrib.auth.models import AbstractUser
# from django.forms import ModelForm
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import *


class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'email')


# class PatientForm(ModelForm):
# 	class Meta:
# 		model = Patient
# 		fields = ('category', 'gender', 'birthdate', 'bio')

# 	def __init__(self, *args, **kwargs):
# 		super(PatientForm, self).__init__(*args, **kwargs)
# 		self.fields['category'].queryset = Category.objects.all()


class PatientForm(forms.ModelForm):
	class Meta:
		model = Patient
		fields = ('categories', 'gender', 'birthdate', 'bio')

		categories = forms.ModelMultipleChoiceField(queryset=Category.objects.all())

	def __init__(self, *args, **kwargs):
		if kwargs.get('instance'):
			initial = kwargs.setdefault('initial', {})
			initial['categories'] = [cat.pk for cat in kwargs['instance'].categories.all()]
		forms.ModelForm.__init__(self, *args, **kwargs)

	def save(self):
		instance = forms.ModelForm.save(self)
		instance.categories.clear()
		instance.categories.add(*self.cleaned_data['categories'])
		return instance


class TherapistForm(forms.ModelForm):
	class Meta:
		model = Therapist
		fields = ('address', 'experience', 'education', 'languages', 'categories', 'gender', 'birthdate', 'bio')


class CustomUserCreationForm(UserCreationForm):
	class Meta:
		model = get_user_model()
		fields = ('username', 'email')


# class ArticleForm(ModelForm):
#     headline = MyFormField(
#         max_length=200,
#         required=False,
#         help_text='Use puns liberally',
#     )

#     class Meta:
#         model = Article
#         fields = ['headline', 'content']