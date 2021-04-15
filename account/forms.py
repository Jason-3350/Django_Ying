from django import forms
from django.core.exceptions import ValidationError
from shop import models
from django.contrib.auth.models import User


class RegForm(forms.Form):
    username = forms.CharField(label="Username", min_length=2, error_messages={"required": "Username can't be empty!",
                                                                               "min_length": "Username length should not small than 2", })
    password = forms.CharField(label='Password', widget=forms.widgets.PasswordInput(),
                               error_messages={"required": "password can't be empty!", })

    re_password = forms.CharField(label='confirm password again', widget=forms.widgets.PasswordInput(),
                                  error_messages={"required": "password can't be empty!", })

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

    def clean_username(self):  # local
        username = self.cleaned_data.get("username")
        if username.isdigit():
            raise ValidationError("Username can't be all digit")
        elif User.objects.filter(username=username):
            raise ValidationError("User already there！")
        else:
            return username

    def clean(self):  # global
        pwd = self.cleaned_data.get('password')
        re_pwd = self.cleaned_data.get('re_password')
        if pwd == re_pwd:
            return self.cleaned_data
        raise ValidationError('Two passwords are inconsistent!!!')


class LogForm(forms.Form):
    username = forms.CharField(
        label="Username",
        error_messages={"required": "Username can't be empty!", })

    password = forms.CharField(
        label="Password",
        widget=forms.widgets.PasswordInput(),
        error_messages={"required": "Password can't be empty!", })

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control '})


class PwdChangeForm(forms.Form):
    old_password = forms.CharField(label='Old password', widget=forms.widgets.PasswordInput(),
                                   error_messages={"required": "Old password can't be empty!", })
    new_password = forms.CharField(label='New Password', widget=forms.widgets.PasswordInput(),
                                   error_messages={"required": "New password can't be empty!", })
    confirm_password = forms.CharField(label='Password Confirmation', widget=forms.widgets.PasswordInput(),
                                       error_messages={"required": "Password Confirmation can't be empty!", })

    # Use clean methods to define custom validation rules

    # def clean_new_password(self):
    #     new_password = self.cleaned_data.get('new_password')
    #     if len(new_password) < 6:
    #         raise forms.ValidationError("Your password is too short.")
    #     elif len(new_password) > 20:
    #         raise forms.ValidationError("Your password is too long.")
    #     return new_password

    def clean_confirm_password(self):
        new_password = self.cleaned_data.get('new_password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if new_password != confirm_password:
            raise forms.ValidationError("Password mismatch. Please enter again.")
        return confirm_password

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control '})
