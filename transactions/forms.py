from django import forms
from .models import Transaction

class TransactionForm(forms.ModelForm):
    class Meta :
        model = Transaction
        fields = [
            
            'user_id',
            'amount',
            'date',
            'account',
            'reference', 

        ]
class TransactionCreate(forms.Form):
    user_id = forms.IntegerField(widget= forms.NumberInput(
        attrs={
            "class":"col-md-4 form-control",
            "type":"hidden",
            "value":0
        }
    ))
    amount = forms.DecimalField(widget= forms.NumberInput(
        attrs={
            "class":"col-md-4 form-control"
        }
    ))
    date = forms.DateField(widget= forms.DateTimeInput(
        attrs={
            "class":"col-md-4 form-control",
            "type" : "date"
        }
    ))
    account = forms.CharField(initial='0',widget= forms.TextInput(
        attrs={
            "class":"col-md-4 form-control",
            "type" : "text"
        }
    ))
    reference = forms.CharField(widget= forms.TextInput(
        attrs={
            "class":"col-md-4 form-control",
            "type" : "text"
        }
    ))
    