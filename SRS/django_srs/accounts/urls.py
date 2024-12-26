from django.urls import path
from . import views

urlpatterns = [
    # URL for user login
    path('login/', views.user_login, name='login'),
    
    # URL for user logout
    path('logout/', views.user_logout, name='logout'),
]

