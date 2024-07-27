from .models import ContactForm
from django import forms


class ContactFormForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ('name', 'email', 'message')