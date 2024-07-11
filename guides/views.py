from typing import Any
from django.shortcuts import render

from .filters import GuideFilter

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import GuideData, Car, Track

class Guides(ListView):
    queryset = GuideData.objects.all()
    
    context_object_name = 'guides'
    template_name = 'Guides/guidesList.html'
    
    # фильтрация данных
    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = GuideFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs
    
    # контекстные данные 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.filterset.form
        
        return context
    
class GuideReview(DetailView):
    car_guides = None
    
    model = GuideData
    context_object_name = 'guide'
    template_name = 'guides/guide.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        guide = self.object
        # Найти все гайды, связанные с той же машиной
        related_guides = GuideData.objects.filter(carName=guide.carName.id)
        context['related_guides'] = related_guides
        context['title'] = context["object"]
        
        return context
    