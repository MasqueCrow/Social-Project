from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView

from accounts import forms
# Create your views here.
class SignUp(CreateView):
    form_class = forms.UserCreationForm
    #Once user has successfully submit their sign up form
    #redirect user to login page
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'
