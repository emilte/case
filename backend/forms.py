from django import forms

class Info(forms.Form):
    applicant = forms.CharField(initial="emil", required=True, widget=forms.HiddenInput)
    name = forms.CharField(initial="Emil Telstad", required=True, min_length=2)
    email = forms.EmailField(initial="emil.telstad@gmail.com", required=True)
    phone = forms.IntegerField(initial="41325358", required=True)
    areacode = forms.IntegerField(initial=7051, required=False, max_value=9999)
    comment = forms.CharField(required=False, widget=forms.Textarea)

    required_css_class = 'required'

    def __init__(self, *args, **kwargs):
        super(type(self), self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
        self.fields['name'].widget.attrs.update({'placeholder': 'Ola Nordmann'})
        self.fields['email'].widget.attrs.update({'placeholder': 'navn@domene.no'})
        self.fields['phone'].widget.attrs.update({'placeholder': 'XXX XX XXX'})
        self.fields['areacode'].widget.attrs.update({'placeholder': '1234'})
