from typing import Any
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from .filters import GuideFilter

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import GuideData, Car, Track

from .utils import PaginateMixin

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

class Guides(PaginateMixin, ListView):
    queryset = GuideData.objects.all()
    
    context_object_name = 'guides'
    template_name = 'Guides/guidesList.html'
    
    @method_decorator(cache_page(60 * 15))  # Кэширование на 15 минут
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
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
    