
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import gettext_lazy as _
from django.shortcuts import render, reverse
from django.views import generic
from django.db.models import Q
from .models import Projekt
from .forms import ProjektModelForm


class ProjektCreateView(LoginRequiredMixin, generic.CreateView, SuccessMessageMixin):
    template_name = "projekt/dashboard_projekt_create.html"
    form_class = ProjektModelForm   
    success_message = _("Projekt erstellt")
    
    def form_valid(self, form):     
        projekt = form.save(commit=False)
        projekt.projekt_ersteller = self.request.user
        projekt.save()
        form.save()
        
        return super(ProjektCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("projekt:list-projekt") 
    
projekt_create_view = ProjektCreateView.as_view()   

class ProjektListView(LoginRequiredMixin, generic.ListView):
    template_name = "projekt/dashboard_projekt.html"
    context_object_name = "projekt"
    
    
    def get_queryset(self): # Suchfunktion und wenn keine Suche zeigt alle Daten an
        
        query = self.request.GET.get('q')
        print (query)
        if query == None:
            object_list = Projekt.objects.all().order_by('-projekt_created') 
            return object_list
        else:
            object_list = Projekt.objects.filter(
                Q(projekt_name__icontains=query) | Q(projekt_nummer__icontains=query) 
            ).order_by('-projekt_created')
            return object_list

projekt_list_view = ProjektListView.as_view() 

class ProjektDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = "projekt/dashboard_projekt_detail.html"
    context_object_name = "projekt"
    
    def get_queryset(self):
        
        user = self.request.user
        queryset = Projekt.objects.filter(projekt_ersteller=user)
        
        return queryset
    
projekt_detail_view = ProjektDetailView.as_view() 
    
class ProjektUpdateView(LoginRequiredMixin, generic.UpdateView, SuccessMessageMixin):
    template_name = "projekt/dashboard_projekt_update.html"
    form_class = ProjektModelForm
    success_message = _("Projekt aktualisiert")
    
    def get_queryset(self):
        user = self.request.user
        queryset = Projekt.objects.filter(projekt_ersteller=user)
        
        return queryset

    def form_valid(self, form):
        item = form.save()
        self.pk = item.pk
        return super(ProjektUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("projekt:detail-projekt", kwargs={'pk': self.pk})

projekt_update_view = ProjektUpdateView.as_view() 

class ProjektDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = "projekt/dashboard_projekt_delete.html"
    # because we are organisor
    def get_success_url(self):
        return reverse("projekt:list-projekt")

    def get_queryset(self):
        user = self.request.user
        queryset = Projekt.objects.filter(projekt_ersteller=user)
        
        return queryset

projekt_delete_view = ProjektDeleteView.as_view() 
    