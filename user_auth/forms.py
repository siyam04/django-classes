from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import TextInput, Select, Textarea

# same app
from user_auth.models import Profile


class SignUpForm(UserCreationForm):
    """Creating Signup Form"""
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        """Customize Signup Form"""
        model = User
        fields=['first_name','last_name','username','email','password1','password2']
        widgets = {
            'username': TextInput(attrs={'class':'form-control'}),
        }


class ProfileForm(forms.ModelForm):
    """Creating Profile Form"""
    class Meta:
        """Customize Profile Form"""
        model = Profile
        fields = '__all__'
        exclude = ['user', ]

        # widgets = {
        #     'profile_name': TextInput(attrs={'class': 'form-control'}),
        #     'email': TextInput(attrs={'class': 'form-control'}),
        # }