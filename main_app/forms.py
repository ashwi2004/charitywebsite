from django import forms
from .models import User, Cause, Donation

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'phone']

class DonationForm(forms.ModelForm):
    phone = forms.CharField(max_length=15)
    donation_type = forms.ChoiceField(choices=[('one_time', 'One-Time'), ('recurring', 'Recurring')])

    cause = forms.ModelChoiceField(
        queryset=Cause.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    amount = forms.DecimalField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'})
    )

    class Meta:
        model = Donation
        fields = ['cause', 'amount']

