from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('csrf/', views.get_csrf),
    path('login/', views.loginView),
    path('logout/', views.logoutView),
    path('signup/', views.signUpView),
]
