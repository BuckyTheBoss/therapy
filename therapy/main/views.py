from django.shortcuts import render

# Create your views here.
def profile_edit(request):
	return render(request, 'profile_edit.html')

def doctor_profile_edit(request):
	return render(request, 'doctor_profile_edit.html')

def doctor_profile(request):
	'''this will have the initial chat space'''
	return render(request, 'doctor_profile.html')

def doctor_index(request):
	'''this will have the initial chat space'''
	return render(request, 'doctor_index.html')





