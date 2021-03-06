from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, PasswordChangeForm
from .models import Account, Club
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.admin.widgets import AdminDateWidget

class AccountCreationForm(UserCreationForm):

    class Meta:
        model = Account
        fields = ('username', 'email','rotaryId','name')

class AccountChangeForm(UserChangeForm):

    class Meta:
        model = Account
        fields = ('username', 'email','rotaryId','name')   

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        self.error_messages['invalid_login'] = 'Incorrect username or password'
        super(LoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Username','autocomplete':'off'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Password'
        }
))

class PasswordChange(PasswordChangeForm):
    error_css_class = 'error'
    old_password = forms.CharField(required=True, 
                    widget=forms.PasswordInput(attrs={
                    'class': 'form-control', 'placeholder': 'Old Password'}))
    new_password1 = forms.CharField(required=True,
                    widget=forms.PasswordInput(attrs={
                    'class': 'form-control', 'placeholder': 'New Password'}))
    new_password2 = forms.CharField(required=True,
                    widget=forms.PasswordInput(attrs={
                    'class': 'form-control', 'placeholder': 'Confirm Password'}))


class ProfileUpdateForm(forms.ModelForm) :
    
    class Meta :
        model = Club
        fields = ['zone','logo','date','meetingPlace']       
        labels = {
        "date": "Charter Date"
        }

    logo = forms.ImageField(required=False, widget=forms.FileInput())
    zone = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'type': 'text',
        'value':0
    }))
    date = forms.DateField(label='Charter Date',required=False, widget=forms.DateInput(attrs={
                    'type': 'date'}))
    

class EmailUpdateForm(forms.ModelForm) :
        
    class Meta :
        model = Account
        fields = ['email','name']       