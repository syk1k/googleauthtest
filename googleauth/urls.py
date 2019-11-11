from django.urls import path
from .views import GoogleAuthView

app_name='googleauth'
urlpatterns = [
    path('', GoogleAuthView.as_view(), name='auth'),    
]
