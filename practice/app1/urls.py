from django.urls import path
from . import views

urlpatterns = [
    path('/',views.login_view,name='login'),
    path('signup/',views.signup_view,name='signup'),
    path('dashboard/',views.dashboard_view,name='dashboard'),
    path('logout/',views.logout_view,name='logout'),
]
