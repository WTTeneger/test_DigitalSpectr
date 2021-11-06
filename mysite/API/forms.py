from django import forms


class form_add_date(forms.Form):
    email = forms.EmailField(label='email')
    phone_number = forms.CharField(label='телефон', max_length=12)
    message = forms.CharField(widget=forms.Textarea, label='сообщение', required=False, max_length=5000)
