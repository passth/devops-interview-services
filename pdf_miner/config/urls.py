from django.urls import path
from core import views

urlpatterns = [
    path('extract-pdf/', views.ExtractPDF.as_view()),
]
