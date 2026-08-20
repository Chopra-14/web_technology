from django import forms
from django.contrib.auth.models import User

from .models import Product


class RegistrationForm(forms.ModelForm):

    password = forms.CharField(
        widget=forms.PasswordInput
    )

    confirm_password = forms.CharField(
        widget=forms.PasswordInput
    )

    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('user', 'User'),
    )

    role = forms.ChoiceField(
        choices=ROLE_CHOICES
    )

    class Meta:
        model = User

        fields = [
            'first_name',
            'last_name',
            'email',
            'password',
            'confirm_password',
        ]

    def clean(self):

        cleaned_data = super().clean()

        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError(
                'Passwords do not match.'
            )

        return cleaned_data

    def save(self, commit=True):

        user = super().save(commit=False)

        # Use email as username
        user.username = self.cleaned_data['email']

        # Hash password
        user.set_password(
            self.cleaned_data['password']
        )

        if commit:
            user.save()

        return user


class LoginForm(forms.Form):

    email = forms.EmailField()

    password = forms.CharField(
        widget=forms.PasswordInput
    )


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product

        fields = [
            'name',
            'quality',
            'quantity'
        ]


class PurchaseForm(forms.Form):

    quantity = forms.IntegerField(
        min_value=1
    )