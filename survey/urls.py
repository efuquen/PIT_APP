from django.urls import path

from . import views

urlpatterns = [
    # Doesn't do anything now
    path('', views.index, name='index'),

    # Individual Observations
    path('observation_ind_new/', views.observation_ind_new, name='observation_ind_new'),
    path('observation_ind_detail/<int:pk>/', views.observation_ind_detail, name='observation_ind_detail'),

    # WIP: General Observations
    path('observation_new/', views.general_observation, name='general_observation'),
    path('observation_detail/<int:pk>/', views.observation_detail, name='observation_detail'),

    # Survey Individual
    path('survey_ind_detail/<int:pk>/', views.survey_ind_detail, name='survey_ind_detail'),
    path('survey_new_ind/', views.survey_individual, name='survey_individual'),

    # Survey
    path('survey_detail/<int:pk>/', views.survey_detail, name='survey_detail'),
    path('survey_new/', views.survey_new, name='survey_new'),
]