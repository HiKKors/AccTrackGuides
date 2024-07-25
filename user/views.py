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
from guides.models import Track, Car

from django.contrib.auth import login

from .forms import UserLoginForms, UserRegistrationForms, UserSetupForm

from django.views.generic.edit import CreateView

from django.views.generic.detail import DetailView

from .mixins import ViewCountMixin

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
        track = Track.objects.get(id=request.POST.get('trackName'))
        car = Car.objects.get(id=request.POST.get('carName'))
        
        user_setup.userId = request.user
        user_setup.trackName = track
        user_setup.carName = car
        user_setup.pass_time = request.POST.get('pass_time')
        
        
        # настройки машины
        
        #TYRES
        lf_psi = request.POST.get('lf_psi')
        lf_toe = request.POST.get('lf_toe')
        lf_camber = request.POST.get('lf_camber')
        lf_caster = request.POST.get('lf_caster')
        
        rf_psi = request.POST.get('rf_psi')
        rf_toe = request.POST.get('rf_toe')
        rf_camber = request.POST.get('rf_camber')
        rf_caster = request.POST.get('rf_caster')
        
        lr_psi = request.POST.get('lr_psi')
        lr_toe = request.POST.get('lr_toe')
        lr_camber = request.POST.get('lr_camber')
        lr_caster = request.POST.get('lr_caster')
        
        rr_psi = request.POST.get('rr_psi')
        rr_toe = request.POST.get('rr_toe')
        rr_camber = request.POST.get('rr_camber')
        rr_caster = request.POST.get('rr_caster')
        
        #ELECTRONICS
        tc = request.POST.get('tc')
        ecumap = request.POST.get('ecumap')
        abs = request.POST.get('abs')
        telemetry_laps = request.POST.get('tel_laps')
        tc2 = request.POST.get('tc2')
        
        #FRONT GRIP
        f_anti_roll_bar = request.POST.get('f_anti_roll')
        brake_power = request.POST.get('brake_power')
        b_bias = request.POST.get('brake_bias')
        steer_ratio = request.POST.get('steer_ratio')
        
        #SUSPENSION
            #front
        lf_wheel_rate = request.POST.get('lf_wheel_rate')
        lf_bump_rate = request.POST.get('lf_bump_rate')
        lf_bump_range = request.POST.get('lf_bump_range')
        
        rf_wheel_rate = request.POST.get('rf_wheel_rate')
        rf_bump_rate = request.POST.get('rf_bump_rate')
        rf_bump_range = request.POST.get('rf_bump_range')

            #rear
        lr_wheel_rate = request.POST.get('lr_wheel_rate')
        lr_bump_rate = request.POST.get('lr_bump_rate')
        lr_bump_range = request.POST.get('lr_bump_range')
        
        rr_wheel_rate = request.POST.get('rr_wheel_rate')
        rr_bump_rate = request.POST.get('rr_bump_rate')
        rr_bump_range = request.POST.get('rr_bump_range')
        
        #REAR GRIP
        r_anti_roll = request.POST.get('r_anti_roll')
        preload_diff = request.POST.get('preload_diff')
        
        #DUMPERS
            #front
        lf_bump = request.POST.get('lf_bump')
        lf_fast_bump = request.POST.get('lf_fast_bump')
        lf_rebound = request.POST.get('lf_rebound')
        lf_fast_rebound = request.POST.get('lf_fast_rebound')
        
        rf_bump = request.POST.get('rf_bump')
        rf_fast_bump = request.POST.get('rf_fast_bump')
        rf_rebound = request.POST.get('rf_rebound')
        rf_fast_rebound = request.POST.get('rf_fast_rebound')

            #rear
        lr_bump = request.POST.get('lr_bump')
        lr_fast_bump = request.POST.get('lr_fast_bump')
        lr_rebound = request.POST.get('lr_rebound')
        lr_fast_rebound = request.POST.get('lr_fast_rebound')
        
        rr_bump = request.POST.get('rr_bump')
        rr_fast_bump = request.POST.get('rr_fast_bump')
        rr_rebound = request.POST.get('rr_rebound')
        rr_fast_rebound = request.POST.get('rr_fast_rebound')
        
        #AERODYNAMICS
            #front
        f_ride_height = request.POST.get('f_ride_height')
        splitter = request.POST.get('splitter')
        f_brake_ducts = request.POST.get('f_brake_ducts')

            #rear
        r_ride_height = request.POST.get('r_ride_height')
        r_wing = request.POST.get('r_wing')
        r_brake_ducts = request.POST.get('r_brake_ducts')

        user_setup.carSettings = {
            "lf_psi": lf_psi,
            "lf_toe": lf_toe,
            "lf_camber": lf_camber,
            "lf_caster": lf_caster,
            "rf_psi": rf_psi,
            "rf_toe": rf_toe,
            "rf_camber": rf_camber,
            "rf_caster": rf_caster,
            "lr_psi": lr_psi,
            "lr_toe": lr_toe,
            "lr_camber": lr_camber,
            "lr_caster": lr_caster,
            "rr_psi": rr_psi,
            "rr_toe": rr_toe,
            "rr_camber": rr_camber,
            "rr_caster": rr_caster,
            "TC": tc,
            "ABS": abs,
            "ECUMap": ecumap,
            "telemetry_laps": telemetry_laps,
            "TC2": tc2,
            "f_antiroll_bar": f_anti_roll_bar,
            "r_antiroll_bar": r_anti_roll,
            "brake_power": brake_power,
            "brake_bias": b_bias,
            "steer_ratio": steer_ratio,
            "lf_wheel_rate": lf_wheel_rate,
            "lf_bumpstop_rate": lf_bump_rate,
            "lf_bumpstop_range": lf_bump_range,
            "rf_wheel_rate": rf_wheel_rate,
            "rf_bumpstop_rate": rf_bump_rate,
            "rf_bumpstop_range": rf_bump_range,
            "lr_wheel_rate": lr_wheel_rate,
            "lr_bumpstop_rate": lr_bump_rate,
            "lr_bumpstop_range": lr_bump_range,
            "rr_wheel_rate": rr_wheel_rate,
            "rr_bumpstop_rate": rr_bump_rate,
            "rr_bumpstop_range": rr_bump_range,
            "preload_diff": preload_diff,
            "lf_bump": lf_bump,
            "lf_fast_bump": lf_fast_bump,
            "lf_rebound": lf_rebound,
            "lf_fast_reb": lf_fast_rebound,
            "rf_bump": rf_bump,
            "rf_fast_bump": rf_fast_bump,
            "rf_rebound": rf_rebound,
            "rf_fast_reb": rf_fast_rebound,
            "lr_bump": lr_bump,
            "lr_fast_bump": lr_fast_bump,
            "lr_rebound": lr_rebound,
            "lr_fast_reb": lr_fast_rebound,
            "rr_bump": rr_bump,
            "rr_fast_bump": rr_fast_bump,
            "rr_rebound": rr_rebound,
            "rr_fast_reb": rr_fast_rebound,
            "r_ride_height": r_ride_height,
            "r_wing": r_wing,
            "r_brake_ducts": r_brake_ducts,
            "f_ride_height": f_ride_height,
            "splitter": splitter,
            "f_brake_ducts": f_brake_ducts
        }
        
        user_setup.save()
        
        
        
    context = {
        'form': form
    }
    return render(request, 'user/addUserSetup.html', context=context)

class UserSetupReview(ViewCountMixin, DetailView):
    model = UserGuide
    context_object_name = 'guide'
    template_name = 'user/userSetup.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        guide = self.object
        # Найти все гайды, связанные с той же машиной
        related_guides = UserGuide.objects.filter(carName=guide.carName.id)
        context['related_guides'] = related_guides
        context['title'] = context["object"]
        
        return context
    
    
class AllCommunitySetups(ListView):
    model = UserGuide
    context_object_name = 'community_setups'
    template_name = 'user/communitySetups.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # собираем все сетапы пользователей
        community_setups = UserGuide.objects.all()
        context['community_setups'] = community_setups
        context['title'] = 'Пользовательские сетапы'
        
        return context