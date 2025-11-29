from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer_name', 'customer_phone']
        widgets = {
            'customer_name': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': "To'liq ismingizni kiriting"
            }),
            'customer_phone': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Telefon raqamingizni kiriting'
            })
        }
