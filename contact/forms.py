from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """Creates Contact form"""

    class Meta:
        model = Contact
        fields = (
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'subject',
            'your_message',
            )
