from django.urls import path
from .views import login, registration, UserSetups, addUserSetup, UserSetupReview

app_name = 'user'

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', registration, name='register'),
    path('mySetups/', UserSetups.as_view(), name='my-setups'),
    path('userSetup/', addUserSetup, name='userSetup'),
    path('userSetupInfo/<int:pk>', UserSetupReview.as_view(), name = 'userSetupInfo')
]