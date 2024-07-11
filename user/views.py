from django.http import HttpResponse
from django.shortcuts import render

from django.shortcuts import render, HttpResponsePermanentRedirect
from django.contrib import auth
from django.urls import reverse

from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

from django.views.generic.list import ListView

from .models import UserGuide

from django.contrib.auth import login

from .forms import UserLoginForms, UserRegistrationForms, UserSetupForm

from django.views.generic.edit import CreateView

# Create your views here.
def login(request):
    if request.method == 'POST':
        form = UserLoginForms(data = request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponsePermanentRedirect(reverse('news'))
    else:
        form = UserLoginForms()
    context = {'form': form}
    return render(request, 'user/login.html', context)

def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForms(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponsePermanentRedirect(reverse('user:login'))
    else:
        form = UserRegistrationForms()
    context = {'form': form}
    return render(request, 'user/register.html', context)
    
    
class UserSetups(ListView):
    queryset = UserGuide.objects.all()
    # context_object_name = 'userSetups'
    template_name = 'user/userSetups.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Находим все сетапы пользователя
        user_id = self.request.user.id
        context['user_setups'] = UserGuide.objects.filter(userId = user_id)
        
        return context
    
def addUserSetup(request):
    form = UserSetupForm()
    user_setup = UserGuide()
    if request.method == 'POST':
        user_setup.userId = request.user.id
        user_setup.trackName = request.POST.get('trackName')
        user_setup.carName = request.POST.get('carName')
        user_setup.pass_time = request.POST.get('pass_time')
        
        # настройки машины
    context = {
        'form': form
    }
    return render(request, 'user/addUserSetup.html', context=context)

# class UserSetupCreateView(CreateView):
#     model = UserGuide
#     form_class = UserSetupForm