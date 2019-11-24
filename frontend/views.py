from django.shortcuts import render, redirect
from django.views import View
from frontend import forms as frontend_forms

class Test(View):
    template = 'frontend/test.html'
    form = frontend_forms.Info

    def get(self, request):
        form = self.form()
        return render(request, self.template, {'form': form})
