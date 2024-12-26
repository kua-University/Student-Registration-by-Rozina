from django import forms


class UserLoginForm(forms.Form):
    """Form for user login."""

    # Username field with styling attributes
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Username"
        })
    )

    # Password field with styling attributes
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Password"
        })
    )
