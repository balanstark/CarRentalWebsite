from django import forms
from carapp.models import Product,Time,Enquiry
from django.core.exceptions import ValidationError

class ProductEmiForm(forms.ModelForm):
    product_name = forms.CharField(disabled=True)
    price = forms.CharField(disabled=True)
    class Meta:
        model = Product
        fields= ['product_name','price']
    loan_amount = forms.IntegerField()
    tenure = forms.IntegerField()

    def clean_tenure(self):
        tenure = self.cleaned_data['tenure']
        if tenure not in [1,2,5,7,10]:
            raise ValidationError("Tenure available only for (1,2,5,7,10) years")
        return tenure

    def clean_loan_amount(self):
        price = self.cleaned_data['price']
        loan_amount = self.cleaned_data['loan_amount']
        if loan_amount > int(price):
            raise ValidationError('Loan amount cannot exceed Price amount')
        return loan_amount
    
class TimeForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        input_formats=['%Y-%m-%d'] )
    class Meta:
        model = Time
        fields = ['time','date']
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'time': forms.Select(attrs={'class': 'form-control'}),
        }

class EnquiryForm(forms.ModelForm):
    class Meta:
        model = Enquiry
        fields = ['concern']