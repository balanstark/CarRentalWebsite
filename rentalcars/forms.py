from django import forms

class RentDetailsForm(forms.Form):
    total_no_of_days = forms.IntegerField(label="Total Number of Days")
    expected_km = forms.IntegerField(label="Expected Km")

class FinalPriceForm(forms.Form):
    total_no_of_days = forms.IntegerField(label="Total Number of Days")
    km_drive_now = forms.IntegerField(label="Current Odometer Reading")
    