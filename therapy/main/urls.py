from django.contrib import admin
from django.urls import path

from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.front, name='front'),
    path('index', views.index, name='index'),
    path('about', views.about, name='about'),

    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('profile_edit/<int:id>', views.profile_edit, name='profile_edit'),

    path('doctor_index', views.doctor_index, name='doctor_index'),
    path('doctor_profile_edit', views.doctor_profile_edit, name='doctor_profile_edit'),
    path('doctor_profile/<int:id>', views.doctor_profile, name='doctor_profile'),

    path('signup/patient/', views.signup, name='patient_signup'),
    path('patient_matched_index', views.patient_matched_index, name='patient_matched_index'),
    path('chat/<int:therapist_id>', views.patient_chat, name='chatroom'),
    path('therapist/chats/<int:therapist_id>', views.all_therapist_chats , name='all_doc_chats'),
    path('therapist/chat/<int:chat_id>', views.therapist_chat, name='doc_chat'),

    path('book/<int:therapist_id>', views.book_session, name='book_session'),

]






