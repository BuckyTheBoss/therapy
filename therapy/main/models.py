from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length=30)


class TherapistProfile(models.Model):
	address = models.TextField()
	experience = IntegerField()
	education = models.CharField(max_length=30)
	languages = models.CharField(max_length=30)
	category = models.ManyToManyField(category)
	gender = models.CharField(max_length=30)
	birthdate = models.DateTimeField()
	bio = models.TextField()

class PatientProfile(models.Model):

	category = models.ManyToManyField(category)
	gender = models.CharField(max_length=30)
	birthdate = models.DateTimeField()
	bio = models.TextField()

class Match(models.Model):

	patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE)
	therapist = models.ForeignKey(TherapistProfile, on_delete=models.CASCADE)
	timestamp = models.DateTimeField(default=timezone.now)

class TherapySession(models.Model):

	match = models.ForeignKey(Match, on_delete=models.CASCADE)
	datetime = models.DateTimeField()
	occured = models.BooleanField()

class SessionLog(models.Model):

	therapist_notes = models.TextField()
	patient_notes = models.TextField()
	therapysession = models.ForeignKey(TherapySession, on_delete=models.SET_NULL, null=True)

class Questionnaire(models.Model):

	q1 = models.TextField()
	q2 = models.TextField()
	q3 = models.TextField()
	q4 = models.TextField()
	q5 = models.TextField()
	a1 = models.TextField()
	a2 = models.TextField()
	a3 = models.TextField()
	a4 = models.TextField()
	a5 = models.TextField()
	match = models.ForeignKey(Match, on_delete=models.CASCADE)