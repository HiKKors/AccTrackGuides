from django.urls import path

from .views import Guides, GuideReview


urlpatterns = [
    path('', Guides.as_view(), name='guides-list'),
    path('<int:pk>', GuideReview.as_view(), name='guide')
]
