from django.shortcuts import render

# Create your views here.

from django.contrib.auth.models import User
from django.views.generic import (
    CreateView,
    
)
from django.urls import reverse_lazy

from .forms import SignupForm

class SignupView(CreateView):
    model = User
    form_class = SignupForm
    template_name = "signup.html"
    success_url = reverse_lazy("index")
    

