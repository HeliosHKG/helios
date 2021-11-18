
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import gettext_lazy as _
from django.shortcuts import render, reverse
from django.views import generic
import csv
from django.db.models import Q
from .models import (
    Projekt, 
    Csv, 
    Gewerk,
    Raumnutzung,
    Gebaudenutzung, 
    Kostenstammdaten_Elektro, 
    Abgabesystem, 
)
from .forms import ProjektModelForm, ProjektSpezModelForm, CsvModelForm


class ProjektCreateView(LoginRequiredMixin, generic.CreateView, SuccessMessageMixin):
    template_name = "projekt/dashboard_projekt_create.html"
    form_class = ProjektModelForm   
    
    
    def form_valid(self, form):     
        projekt = form.save(commit=False)
        projekt.projekt_ersteller = self.request.user
        projekt.save()
        form.save()
        
        return super(ProjektCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("projekt:list-projekt") 
        # return reverse("projekt:detail-submission", kwargs={'pk': self.pk})
    
projekt_create_view = ProjektCreateView.as_view()   

class ProjektListView(LoginRequiredMixin, generic.ListView):
    template_name = "projekt/dashboard_projekt.html"
    context_object_name = "projekt"
    
    
    def get_queryset(self): # Suchfunktion und wenn keine Suche zeigt alle Daten an
        
        query = self.request.GET.get('q')
        
        if query == None:
            object_list = Projekt.objects.all()
            return object_list
        else:
            object_list = Projekt.objects.filter(
                Q(projekt_name__icontains=query) | Q(projekt_nummer__icontains=query) 
            )
            return object_list

projekt_list_view = ProjektListView.as_view() 

# Eventuell wird dies noch benötigt

# class ProjektDetailView(LoginRequiredMixin, generic.DetailView):
#     template_name = "projekt/dashboard_projekt_detail.html"
#     context_object_name = "projekt"
    
#     def get_queryset(self):
        
#         user = self.request.user
#         queryset = Projekt.objects.filter(projekt_ersteller=user)
        
#         return queryset
    
# projekt_detail_view = ProjektDetailView.as_view() 
    
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
    
    def get_success_url(self):
        return reverse("projekt:list-projekt")

    def get_queryset(self):
        user = self.request.user
        queryset = Projekt.objects.filter(projekt_ersteller=user)
        
        return queryset

projekt_delete_view = ProjektDeleteView.as_view() 

#projektspezifikation

class ProjektSpezCreateView(LoginRequiredMixin, generic.CreateView, SuccessMessageMixin):
    template_name = "projekt/dashboard_projektSpez_create.html"
    form_class = ProjektSpezModelForm   
    
    
    def form_valid(self, form):     
        projekt_pk = self.kwargs['pk']
        projekt = form.save(commit=False)
        projekt.projekt_name_id = projekt_pk
        projekt.save()
        
        form.save()
        
        return super(ProjektSpezCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("projekt:list-projekt") 
    
projekt_createSpez_view = ProjektSpezCreateView.as_view()   


#File Handler
#Gewerk
def upload_file_gewerk(request):  
    
    form = CsvModelForm(request.POST or None, 
                        request.FILES or None) 
    
    if form.is_valid():
        form.save()
        form = CsvModelForm()
        obj = Csv.objects.get(activated=False)
        
        with open(obj.file_name.path, 'r') as f:
            reader = csv.reader(f)
            
            for i, row in enumerate(reader):
                if i==0:
                    pass
                    
                else:
                    row = "".join(row)
                    row = row.replace(" ", "")
                    row = row.replace(";", " ")
                    row = row.split()
                    
                    Gewerk.objects.create(
                        
                        gewerk = row[1],
                        
                    )

                    
            obj.activated = True
            obj.save()
    
    return render (request, 'projekt/stammdaten_gewerk.html' , {'form': form,})

#Stammdaten Raumnutzung
def upload_file_raumnutzung(request):  
    
    form = CsvModelForm(request.POST or None, 
                        request.FILES or None) 
    
    if form.is_valid():
        form.save()
        form = CsvModelForm()
        obj = Csv.objects.get(activated=False)
        
        with open(obj.file_name.path, 'r') as f:
            reader = csv.reader(f)
            
            for i, row in enumerate(reader):
                if i==0:
                    pass
                    
                else:
                    row = "".join(row)
                    row = row.replace(" ", "")
                    row = row.replace(";", " ")
                    row = row.split()
                    
                    Raumnutzung.objects.create(
                        
                        raumnutzung = row[1],
                        
                    )

                    
            obj.activated = True
            obj.save()
    
    return render (request, 'projekt/stammdaten_raumnutzung.html' , {'form': form,})

#Stammdaten Gebäudenutzung 
def upload_file_gebauedenutzung(request):  
    
    form = CsvModelForm(request.POST or None, 
                        request.FILES or None) 
    
    if form.is_valid():
        form.save()
        form = CsvModelForm()
        obj = Csv.objects.get(activated=False)
        
        with open(obj.file_name.path, 'r') as f:
            reader = csv.reader(f)
            
            for i, row in enumerate(reader):
                if i==0:
                    pass
                    
                else:
                    row = "".join(row)
                    row = row.replace(" ", "")
                    row = row.replace(";", " ")
                    row = row.split()
                    
                    Gebaudenutzung.objects.create(
                        
                        gebaudenutzung = row[1],
                        
                    )

                    
            obj.activated = True
            obj.save()
    
    return render (request, 'projekt/stammdaten_gebauedenutzung.html' , {'form': form,})

#Stammdaten Kosten Elektro 
def upload_file_kosten_elektro(request):  
    
    form = CsvModelForm(request.POST or None, 
                        request.FILES or None) 
    
    if form.is_valid():
        form.save()
        form = CsvModelForm()
        obj = Csv.objects.get(activated=False)
        
        with open(obj.file_name.path, 'r') as f:
            reader = csv.reader(f)
            
            for i, row in enumerate(reader):
                if i==0:
                    pass
                    
                else:
                    row = "".join(row)
                    row = row.replace(" ", "")
                    row = row.replace(";", " ")
                    row = row.split()
                    
                    res_geb:Gebaudenutzung 
                    gebauedenutzung = Gebaudenutzung.objects.get(gebaudenutzung = row[1])
                    
                    if gebauedenutzung != 0:
                        res_geb = gebauedenutzung
                    else: 
                        pass
                    
                    res_raum:Raumnutzung
                    raumnutzung = Raumnutzung.objects.get(raumnutzung = row[2])
                    if raumnutzung != 0:
                        res_raum = raumnutzung
                    else:
                        pass
                    res_gewerk:Gewerk
                    gewerk = Gewerk.objects.get(gewerk = row[3])
                    if gewerk != 0:
                        res_gewerk = gewerk
                    else:
                        pass
                    
                    
                    data = Kostenstammdaten_Elektro.objects.create(
                        
                        
                        
                        einheitspreis_pro_m2 = row[4],
                        
                    )
                    
                    data.gebaudenutzung = res_geb
                    data.gewerk = res_gewerk
                    data.raumnutzung = res_raum
                    data.save()
                    
                    
            obj.activated = True
            obj.save()
    
    return render (request, 'projekt/stammdaten_kosten_elektro.html' , {'form': form,})


#Stammdaten Abgabesystem 
def upload_file_kosten_elektro(request):  
    
    form = CsvModelForm(request.POST or None, 
                        request.FILES or None) 
    
    if form.is_valid():
        form.save()
        form = CsvModelForm()
        obj = Csv.objects.get(activated=False)
        
        with open(obj.file_name.path, 'r') as f:
            reader = csv.reader(f)
            
            for i, row in enumerate(reader):
                if i==0:
                    pass
                    
                else:
                    row = "".join(row)
                    row = row.replace(" ", "")
                    row = row.replace(";", " ")
                    row = row.split()
                    
                    res_geb:Gebaudenutzung 
                    gebauedenutzung = Gebaudenutzung.objects.get(gebaudenutzung = row[1])
                    
                    if gebauedenutzung != 0:
                        res_geb = gebauedenutzung
                    else: 
                        pass
                    
                  
                    
                    
                    data = Abgabesystem.objects.create(
                        
                        
                        
                        einheitspreis_pro_m2 = row[4],
                        
                    )
                    
                    data.gebaudenutzung = res_geb
                    data.gewerk = res_gewerk
                    data.raumnutzung = res_raum
                    data.save()
                    
                    
            obj.activated = True
            obj.save()
    
    return render (request, 'projekt/stammdaten_abgabesystem.html' , {'form': form,})