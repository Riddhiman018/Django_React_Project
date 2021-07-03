from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.UserSheet,name = "API_look"),
    path('verify',views.user_validation_sheet,name = "Validation")
]