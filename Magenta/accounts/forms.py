from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from home.models import Company

class UserLoginForm(forms.Form):
    # Form to be used to log users in
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class forgotForm(forms.Form):
    Email = forms.EmailField()

    Email.widget.attrs.update({'class': 'form-control','name' :'search','placeholder':'Email address'})

    def __str__(self):
        return self.Email

class UserForm(ModelForm):
    class Meta:
        model = Company
        fields = ('name','organisation','email','Intro','document','contact','CIN','logo' ,'password','selfie')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class' :'input--style-5','type':'text','name':'name'})
        self.fields['email'].widget.attrs.update({'class' :'input--style-5','type':'email','name':'email'})
        self.fields['password'].widget.attrs.update({'class' :'input--style-5','type':'password','name':'password'})
        self.fields['selfie'].widget.attrs.update({'class' :'custom-file-input','type':'file','id':'inputGroupFile'})
        self.fields['organisation'].widget.attrs.update({'class' :'input--style-5','type':'text','name':'company'})
        self.fields['Intro'].widget.attrs.update({'class' :'form-control','id':'exampleFormControlTextarea1', 'rows':'4 '})
        self.fields['document'].widget.attrs.update({'class' :'custom-file-input','type':'file','id':'inputGroupFile'})
        self.fields['contact'].widget.attrs.update({'class' :'input--style-5','type':'number','name':'number','style':'width: 100%;'})
        self.fields['CIN'].widget.attrs.update({'class' :'input--style-5','type':'text','name':'number'})
        self.fields['logo'].widget.attrs.update({'class' :'custom-file-input','type':'file','id':'inputGroupFile'})

class UserRegistrationForm(UserCreationForm):
    # Form used to register the user
    firstname = forms.CharField(label="First Name")
    lastname = forms.CharField(label="Last Name")
    password1 = forms.CharField(
        label="Password", 
        widget=forms.PasswordInput)
        
    password2 = forms.CharField(
        label="Confirm Password", 
        widget=forms.PasswordInput)
        
    
    class Meta:
        model = User
        fields = ['firstname', 'lastname', 'email', 'username', 'password1', 'password2']
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if User.objects.filter(email=email).exclude(username=username):
            raise forms.ValidationError(u'Email address must be unique')
        return email
        
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        
        if not password1 or not password2:
            raise ValidationError("Please confirm your password")
            
        if password1 != password2:
            raise ValidationError("Passwords must match")
        
        return password2
        