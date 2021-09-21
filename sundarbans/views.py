from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, FormView
from .models import WildLife, Guide, Spot
from .forms import BookingForm


# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'


class WildLifeView(ListView):
    model = WildLife
    template_name = 'sundarbans/wildlife.html'


class GuideView(ListView):
    model = Guide
    template_name = 'sundarbans/guide.html'


class SpotView(ListView):
    model = Spot
    template_name = 'sundarbans/spot.html'


# @login_required
@permission_required(perm='',login_url='login')
def BookingFormView(request):
    form = BookingForm()
    login_url = 'login'
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home_')
    return render(request, 'booking form.html', {'form': form})
