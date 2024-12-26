import json
from django.views.generic import DetailView
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from main.models import Prijave
from .forms import PutovanjeForm

## Create your views here.

from main.models import Putovanje

class PutovanjeList(ListView):
    model = Putovanje

    def post(self, request, *args, **kwargs):
        object_id = request.POST.get('object_id')
        obj = get_object_or_404(Putovanje, putovanje_sifraPutovanja=object_id)
        obj.delete()
        return redirect('putovanja')
    
class PutovanjaCroatiaList(ListView):
    model = Putovanje
    template_name = 'main/putovanje_list.html'
    
    def get_queryset(self):
        return Putovanje.objects.filter(putovanje_drzava='Croatia')

    def post(self, request, *args, **kwargs):
        object_id = request.POST.get('object_id')
        obj = get_object_or_404(Putovanje, putovanje_sifraPutovanja=object_id)
        obj.delete()
        return redirect('putovanja_hr')

class PrijaveList(ListView):
    model = Prijave

class PutovanjeDetailView(DetailView):
    model = Putovanje
    template_name = 'main/putovanje_detail.html'  
    context_object_name = 'putovanje' 

    def get_object(self):
        return get_object_or_404(Putovanje, putovanje_sifraPutovanja=self.kwargs['putovanje_sifraPutovanja'])

def index(request):
    return render(request, 'base_generic.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')

    else:
        form = UserCreationForm()

    context = {'form': form}

    return render(request, 'registration/register.html', context)

def add_putovanje(request):
    if request.method == 'POST':
        form = PutovanjeForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('putovanja') 
    else:
        form = PutovanjeForm()

    return render(request, 'main/form.html', {'form': form})

def update_putovanje(request, pk):
    putovanje = get_object_or_404(Putovanje, pk=pk)
    if request.method == 'POST':
        form = PutovanjeForm(request.POST, instance=putovanje)
        if form.is_valid():
            entry = form.save()
            return redirect('putovanje_detail', putovanje_sifraPutovanja=entry.pk)
    else:
        form = PutovanjeForm(instance=putovanje)
    return render(request, 'main/form.html', {'form': form})