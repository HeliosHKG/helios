from django.shortcuts import render, reverse
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import gettext_lazy as _

from helios.vorstudie.forms import (
    LeistungModelForm,
    InvestitionskostenModelForm, 
)


class VorstudieView(generic.ListView):
    template_name = "vorstudie/dashboard_vorstudie.html"
    

    def get_success_url(self):
        return reverse("vorstudie:dashboard-project") 
    
vorstudie_view = VorstudieView.as_view()

# Leistung
class LeistungCreateView(LoginRequiredMixin, generic.CreateView, SuccessMessageMixin):
    template_name = "vorstudie/dashboard_leistung_create.html"
    form_class = LeistungModelForm   
    
    def form_valid(self, form):     
        projekt = form.save(commit=False)
        projekt.projekt_ersteller = self.request.user
        projekt.save()
        form.save()
        
        return super(LeistungCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("projekt:list-projekt") #Return noch definieren
    
leistung_create_view = LeistungCreateView.as_view()

# Investitionskosten
class InvestitionskostenCreateView(LoginRequiredMixin, generic.CreateView, SuccessMessageMixin):
    template_name = "vorstudie/dashboard_investitionskosten_create.html"
    form_class = InvestitionskostenModelForm   
    
    def form_valid(self, form):     
        projekt = form.save(commit=False)
        projekt.projekt_ersteller = self.request.user
        projekt.save()
        form.save()
        
        return super(LeistungCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("projekt:list-projekt") #Return noch definieren
    
investitionskosten_create_view = InvestitionskostenCreateView.as_view()