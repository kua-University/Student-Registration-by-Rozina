from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import UserLoginForm

# Create your views here.

def user_login(request):
    """Handle user login."""
    forms = UserLoginForm()

    # Check if the request method is POST
    if request.method == "POST":
        # Bind data from the request to the form
        forms = UserLoginForm(request.POST)

        # Validate the form data
        if forms.is_valid():
            # Extract username and password from cleaned data
            username = forms.cleaned_data["username"]
            password = forms.cleaned_data["password"]

            # Authenticate the user
            user = authenticate(username=username, password=password)

            # Check if authentication was successful
            if user:
                # Log the user in
                login(request, user)
                # Redirect to the home page upon successful login
                return redirect("home")
            else:
                # Show an error message if login fails
                messages.error(request, "Invalid Username or Password")
                # Redirect back to the login page
                return redirect("login")

    # Prepare the context for rendering the login page
    context = {
        "forms": forms
    }

    # Render the login template with the context
    return render(request, "accounts/login.html", context)


def user_logout(request):
    """Handle user logout."""
    # Log the user out
    logout(request)
    # Redirect to the login page after logging out
    return redirect("login")