import datetime

from django import forms
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from tempus_dominus.widgets import DatePicker, TimePicker, DateTimePicker

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


class AppoinmentForm(forms.Form):
    # date_field = forms.DateField(widget=DatePicker())
    # Available_dates = forms.DateField(
    #     required=True,
    #     widget=DatePicker(
    #         options=
    #         {
    #         'daysOfWeekDisabled': [1,4],
    #         }, 'sideBySide'=True,
    #         # options={
    #         #     'minDate': 'today',
    #         #     'maxDate': '2020-01-01',
    #         # },
            
    #     ),
    # )
    # Select_a_time = forms.TimeField(
    #     widget=TimePicker(
    #         options={
    #             'enabledHours': [9, 10, 11, 12, 13, 14, 15, 16],
    #         },
    #         attrs={
    #             'input_toggle': True,
    #             'input_group': True,
    #         },
       
    #     ),
    # )
    Select_an_available_session = forms.DateTimeField(
        widget=DateTimePicker(
            options={
                'minDate': (
                    datetime.date.today() + datetime.timedelta(days=1)
                ).strftime(
                    '%Y-%m-%d'
                ),  # Tomorrow
                'useCurrent': True,
                'collapse': False,
                'sideBySide': True,
                'daysOfWeekDisabled': [0,2,4,5,6],
                'enabledHours': [10, 11, 12],

            },
            attrs={
                'append': 'fa fa-calendar',
                'icon_toggle': True,
            }
        ),
    )