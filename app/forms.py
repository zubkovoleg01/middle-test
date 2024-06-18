from django import forms


class PhoneNumberForm(forms.Form):
    phone_number = forms.CharField(label='Номер телефона', max_length=11, min_length=11)