from django.urls import path
from .views import login, registration, UserSetups, addUserSetup, UserSetupReview, AllCommunitySetups, Profile, AccountDetailUpdateView, FavoriteSetupsView, UserPasswordChangeView

from django.contrib.auth.views import LogoutView


app_name = 'user'

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', registration, name='register'),
    path('mySetups/', UserSetups.as_view(), name='my-setups'),
    path('userSetup/', addUserSetup, name='userSetup'),
    path('userSetupInfo/<int:pk>', UserSetupReview.as_view(), name = 'userSetupInfo'),
    path('community-setups', AllCommunitySetups.as_view(), name='community_setups'),
    path('profile/<int:pk>', Profile.as_view(), name='profile'),
    path('profile/edit-account/<int:pk>', AccountDetailUpdateView.as_view(), name='edit-account'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/favorites/<int:pk>', FavoriteSetupsView.as_view(), name='favorites'),
    path('profile/change-password/<int:pk>', UserPasswordChangeView.as_view(), name='password_change' )
]