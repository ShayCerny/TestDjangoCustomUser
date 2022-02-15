from pyexpat import model
from django.shortcuts import redirect, render
from .models import User
from .forms import SignupForm, LoginForm
from django.contrib.auth import login, logout
from django.views.generic import CreateView, ListView

# Create your views here.


# Class based View
class SignupView(ListView):
    model='User'
    template_name='signup.html'


# Function based View
def signUpView (request):
    if request.method == "POST":
        # Get Form Data
        form = SignupForm(request.POST)
        if form.is_valid():
        # Create new user with form data
            newUser = User()
            newUser.name = form.cleaned_data['name']
            newUser.email = form.cleaned_data['email']
            newUser.password = form.cleaned_data['password']
        # Save new user
            newUser.save()
            login(request, newUser)
        # Redirect to index
        return redirect('home')
    else:
        form = SignupForm()
        return render(request, 'signup.html', {'form': form})


def loginView (request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            user = User.objects.get(email=email)
            if user.password == form.cleaned_data['password']:
                login(request, user)
        return redirect('home')
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})


def logoutView (request):
    logout(request)
    return redirect('home')

def index (request):
    users = User.objects.all()
    return render(request, 'index.html', {'users': users})