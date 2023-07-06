from django import forms
from .models import *

class AddForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category_name', 'item_name', 'total_quantity', 'issued_quantity', 'received_quantity', 'unit_price']
        widgets = {
            'item_name': forms.TextInput(attrs={'class': 'form-control'}),
            'total_quantity': forms.TextInput(attrs={'class': 'form-control'}),
            'issued_quantity': forms.TextInput(attrs={'class': 'form-control'}),
            'received_quantity': forms.TextInput(attrs={'class': 'form-control'}),
            'unit_price': forms.TextInput(attrs={'class': 'form-control'}),
}

class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ["quantity", "amount_received", "unit_price", "issued_to"]
        widgets = {
            'quantity': forms.TextInput(attrs={'class': 'form-control'}),
            'amount_received': forms.TextInput(attrs={'class': 'form-control'}),
            'issued_to': forms.TextInput(attrs={'class': 'form-control'}),
            'unit_price': forms.TextInput(attrs={'class': 'form-control'}),
}