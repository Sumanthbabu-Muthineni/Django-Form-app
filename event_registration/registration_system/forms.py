from django import forms
from .models import Registration

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['full_name', 'email', 'phone_number', 'event_sessions']
        app_label = 'registration_system'