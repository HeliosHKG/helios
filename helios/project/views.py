from django.shortcuts import render
from django.views import generic
from .models import Projekt


class PorjectView(generic.View):

    model = Projekt

    def get_queryset(self):
        
        query = "Test"
        
        
        return super(PorjectView).get_queryset()
    
project_view = PorjectView.as_view()