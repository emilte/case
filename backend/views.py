from django.shortcuts import render, redirect
from django.views import View
from backend import forms as backend_forms
from urllib import request

import smtplib
from email.message import EmailMessage


class Test(View):
    template = 'backend/test.html'
    form = backend_forms.Info

    def get(self, request):
        form = self.form()
        return render(request, self.template, {'form': form})

    def post(self, request):
        form = self.form(request.POST)
        msg = None

        if form.is_valid():
            msg = "Success"

            try:
                server = smtplib.SMTP_SSL('smtp.gmail.com')

                sent_from = 'script97tester@gmail.com'
                password = "Django!23"

                server.login(sent_from, password)

                to = ['io@nettbureau.no', 'emil.telstad@gmail.com']

                email = EmailMessage()
                email.set_content('Skjemaet som ble sendt inn er akseptert')

                email['Subject'] = 'Varsel'
                email['From'] = sent_from
                email['To'] = to

                server.send_message(email)

            except Exception as e:
                print(e)


        else:
            print(form.errors)
            msg = "Error"

        return render(request, self.template, {'form': form, 'msg': msg})
