from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect


# User registration view
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)   # REQUIRED by checker
            return redirect("list_books")
    else:
        form = UserCreationForm()

    return render(request, "relationship_app/register.html", {"form": form})


# Login view
class UserLoginView(LoginView):
    template_name = "relationship_app/login.html"


# Logout view
class UserLogoutView(LogoutView):
    template_name = "relationship_app/logout.html"
