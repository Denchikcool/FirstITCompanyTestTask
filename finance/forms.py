from django import forms
from .models import Transaction

class TransactionFrom(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = "__all__"