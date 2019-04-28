from django.shortcuts import render

# Create your views here.
def profile_edit(request):
	return render(request, 'profile_edit.html')


def doctor_profile_edit(request):
	return render(request, 'doctor_profile_edit.html')


