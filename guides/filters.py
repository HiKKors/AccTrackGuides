import django_filters
from .models import GuideData

class GuideFilter(django_filters.FilterSet):
    
    class Meta:
        model = GuideData
        fields = {
            'trackName__name': ['icontains'],
            'carName__name': ['icontains']
        }