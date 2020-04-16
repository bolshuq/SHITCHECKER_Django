from django.urls import path
from . import views
app_name ="Checker"
urlpatterns = [
    path('', views.add_card,name='add_card'),
    path('card/<str:pk>/', views.checkmyvisa,name='checkmyvisa'),
]
