from django.contrib import admin
from django.urls import path, include
from frontend import views as frontend_views
from backend import views as backend_views
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='case/index.html')),
    path('frontend/', frontend_views.Test.as_view(), name="frontend"),
    path('backend/', backend_views.Test.as_view(), name="backend"),

]
