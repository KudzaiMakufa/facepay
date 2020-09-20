from django import forms
class DepositForm(forms.Form):

    recipient = forms.IntegerField(widget= forms.NumberInput(
        attrs={
            "class":"col-md-4 form-control",
            
        }
    ))
    amount = forms.DecimalField(widget= forms.NumberInput(
        attrs={
            "class":"col-md-4 form-control"
        }
    ))