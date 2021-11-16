from django.shortcuts import render
from django.views import generic
from .models import Projekt


class PorjectView(generic.Templateview):

    model = Projekt

    def get_queryset(self):
        
        query = "Test_Update"
        
        
        return super(PorjectView).get_queryset()
    
 