from django.shortcuts import render
from django.views import generic
from .models import Vorstudie


class VorstudieView (generic.Templateview):

    model = Vorstudie

    def get_queryset(self):
        
        
        return super(VorstudieView).get_queryset()
    
 
