from django.shortcuts import render, reverse
from django.views import generic
from .models import Vorstudie


class VorstudieView(generic.ListView):
    template_name = "vorstudie/dashboard_vorstudie.html"
    model = Vorstudie

    def get_success_url(self):
        return reverse("vorstudie:dashboard-project") 
    
vorstudie_view = VorstudieView.as_view()
