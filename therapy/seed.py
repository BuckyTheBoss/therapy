from main.models import *
from faker import Faker
import random

fake = Faker()

def gen_fname():
	return fake.first_name()

def gen_lname():
	return fake.last_name()

def gen_password():
	return fake.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True)

def gen_paragraph():
	return fake.paragraph(nb_sentences=5, variable_nb_sentences=True, ext_word_list=None)

def gen_sentance():
	return fake.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None)

def pick_user():
	return random.choice(User.objects.all())

def gen_datetime(datetime=None):
	if datetime != None:
		return fake.date_time_between(start_date=datetime, end_date="-18d", tzinfo=None)
	return fake.date_this_year(before_today=True, after_today=False)

def gen_birthdate():
	return fake.date_this_century(before_today=True, after_today=False)

def pick_category():
	return random.choice(Category.objects.all())

def create_patient_users(number):
	'''create x users'''
	for i in range(0, number):
		fname = gen_fname()
		lname = gen_lname()
		username = fname.lower() + lname.lower()
		user = User.objects.create_user(username=username, password=gen_password(), first_name=fname, last_name=lname, is_patient=True)
		user.save()

def seed_patient_profile():
	for profile in Patient.objects.all():
		profile.category.add(pick_category())
		profile.bio = gen_sentance()
		profile.birthdate = gen_birthdate()
		profile.gender = random.choice(['M','F']) 
		profile.save()

def create_categories():
	wordlist = ['Family','Trauma', 'Marriage', 'Work', 'Life']
	for word in wordlist:
		cat = Category(name=word)
		cat.save()

