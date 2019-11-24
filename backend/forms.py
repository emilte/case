from django import forms
from urllib import request
from captcha.fields import ReCaptchaField
from django.conf import settings

def between(x, a, b):
    return x >= a and x <= b

class Info(forms.Form):
    applicant = forms.CharField(initial="emil", required=True, widget=forms.HiddenInput)
    name = forms.CharField(initial="Emil Telstad", required=True, min_length=2)
    email = forms.EmailField(initial="emil.telstad@gmail.com", required=True)
    phone = forms.IntegerField(initial="41325358", required=True)
    areacode = forms.CharField(initial="7051", required=False, min_length=4, max_length=4)
    comment = forms.CharField(required=False, widget=forms.Textarea)
    captcha = ReCaptchaField(
        public_key=settings.RECAPTCHA_PUBLIC_KEY,
        private_key=settings.RECAPTCHA_PRIVATE_KEY,
    )

    required_css_class = 'required'

    def __init__(self, *args, **kwargs):
        super(type(self), self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
        self.fields['name'].widget.attrs.update({'placeholder': 'Ola Nordmann'})
        self.fields['email'].widget.attrs.update({'placeholder': 'navn@domene.no'})
        self.fields['phone'].widget.attrs.update({'placeholder': '12345678'})
        self.fields['areacode'].widget.attrs.update({'placeholder': '1234'})

    def clean_phone(self):
        data = self.cleaned_data['phone']

        if between(data, 40000000, 49999999) or between(data, 90000000, 99999999):
            return data

        raise forms.ValidationError("Invalid Norwegian phone number")

    def clean_areacode(self):
        data = self.cleaned_data['areacode']
        if not data: # Areacode is not required
            return data

        try: int(data)
        except: raise forms.ValidationError("Areacodes contain only digits (0-9)")

        if len(data) != 4:
            raise forms.ValidationError("Norwegian areacodes contain exactly 4 digits")

        resource = request.urlopen("https://www.bring.no/postnummerregister-ansi.txt")
        encode = resource.headers.get_content_charset()
        for line in resource:
            line = line.decode(encode)
            n = line.split('\t')[0]
            if int(n) == int(data):
                return data

        raise forms.ValidationError("Areacode does not exist")
