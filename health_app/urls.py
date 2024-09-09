from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import predict_disease
from django.urls import path
from .views import generate_report
urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('report-symptoms/', views.report_symptoms, name='report_symptoms'),
    path('predict/<int:report_id>/', views.predict_disease, name='predict_disease'),
    path('view-report/<int:report_id>/', views.view_report, name='view_report'),
    path('symptom-list/', views.symptom_list, name='symptom_list'),
    path('predict/<int:report_id>/', views.predict_disease, name='predict_disease'),
    path('welcome/', views.welcome_page, name='welcome'),  # Welcome page URL
    path('terms-and-conditions/', views.terms_and_conditions, name='terms_and_conditions'),
    path('about/', views.about, name='about'),
    path('initialize_chatbot/', views.initialize_chatbot, name='initialize_chatbot'),
    path('chat/', views.chat, name='chat'),
    path('report/<int:global_id>/', views.generate_report, name='generate_report'),# path('follow-up/<int:disease_id>/', views.follow_up_questions, name='follow_up'),
    path('medical-history/', views.medical_history_view, name='medical_history'),
     path('capture-location/', views.capture_location, name='capture_location'),
    # path('follow-up/<int:disease_id>/', views.follow_up_questions, name='follow_up'),
    
]
    


