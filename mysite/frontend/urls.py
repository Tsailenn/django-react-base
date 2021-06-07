from django.urls import path
from . import views

'''
Add paths for redirection here. If necessary.
'''
urlpatterns = [
    path('', views.index)
]