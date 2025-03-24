from django.urls import path
from studentapp import views

urlpatterns = [
    path('student/', views.display_view),
]
