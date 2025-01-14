from django import forms
from .models import Membership
from django.utils.timezone import now

class MembershipPurchaseForm(forms.ModelForm):
    username = forms.CharField(label="Username", disabled=True)
    membership_id = forms.ModelChoiceField(
        queryset=Membership.objects.all(), 
        label="Select Membership", 
        widget=forms.Select(attrs={"class": "form-control"})
    )
    purchase_date = forms.DateField(
        label="Purchase Date", 
        initial=now().date(),
        widget=forms.DateInput(attrs={"type": "date", "class": "form-control"})
    )
    start_date = forms.DateField(
        label="Start Date", 
        widget=forms.DateInput(attrs={"type": "date", "class": "form-control"})
    )
    class Meta:
        model=Membership
        fields= ('price',)
