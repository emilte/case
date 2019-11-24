from django.shortcuts import render, redirect
from django.views import View
from backend import forms as backend_forms

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
            print('Yess')
        else:
            msg = "Error"

        return render(request, self.template, {'form': form, 'msg': msg})
