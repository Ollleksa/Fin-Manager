from django import forms


class Update_Balance(forms.Form):
    new_balance = forms.DecimalField(max_digits=20, decimal_places=2)

