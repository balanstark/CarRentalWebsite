from django import forms
from django.contrib.auth.models import User
from userformapp.models import UserDetails
from django_recaptcha.fields import ReCaptchaField
from django.core.exceptions import ValidationError

class UserForm(forms.ModelForm):
    password = forms.CharField(max_length=100,widget=forms.PasswordInput)
    class Meta:
        model = User
        # fields = '__all__'

        fields = ['email','username','password']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserDetails
        fields = ['phone','door_no','street','landmark','city','state','pincode','userpic']
    captcha = ReCaptchaField()

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email']

class UserProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserDetails
        fields = ['phone','door_no','street','landmark','city','state','pincode','userpic']

class PasswordResetForm(forms.Form):
    username = forms.CharField(max_length=100)
    new_password = forms.CharField(max_length=100, widget=forms.PasswordInput)
    confirm_password = forms.CharField(max_length=100, widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get('new_password')
        confirm_password = cleaned_data.get('confirm_password')

        if new_password and confirm_password and new_password != confirm_password:
            raise ValidationError("New password and Confirm password do not match")
        return cleaned_data