from django.contrib import admin
from django.urls import path

from . import views
from django.contrib.auth import views as auth_views




urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile_edit/<int:id>', views.profile_edit, name='profile_edit'),
    path('doctor_profile_edit', views.doctor_profile_edit, name='doctor_profile_edit'),
    path('doctor_profile', views.doctor_profile, name='doctor_profile'),
    path('doctor_index', views.doctor_index, name='doctor_index'),
    path('index', views.index, name='index'),
    path('signup/patient/', views.signup, name='patient_signup'),
    path('patient_matched_index', views.patient_matched_index, name='patient_matched_index'),

    path('front', views.front, name='front'),

    path('chat/<int:therapist_id>', views.patient_chat, name='chatroom'),

]



