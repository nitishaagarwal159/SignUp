from django import forms

class User_Signup(forms.Form):
    username=forms.CharField(label='username',max_length=200)
    password=forms.CharField(label='password',max_length=500)
