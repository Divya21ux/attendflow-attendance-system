from django.urls import path
from .views import predict_attendance, front, signin, dashboard

urlpatterns = [
    path('', front, name='front'),                    
    path('signin/', signin, name='signin'), 
    path('dashboard/', dashboard, name='dashboard'),          
    path('predict/', predict_attendance, name='predict_attendance'),

]

