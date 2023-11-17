from django import forms
from phonenumber_field.formfields import PhoneNumberField

from .models import Order, Program


class OrderForm(forms.ModelForm):
    phone = PhoneNumberField(label='Телефон')

    class Meta:
        model = Order
        fields = ('name', 'phone', 'email')

