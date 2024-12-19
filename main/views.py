from django.views.generic import DetailView
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

## Create your views here.

from main.models import Putovanje

class PutovanjeList(ListView):
    model = Putovanje

from main.models import Prijave

class PrijaveList(ListView):
    model = Prijave



class PutovanjePrijaveList(ListView):
    template_name = 'main/prijave_by_putovanja.html'

    def get_queryset(self):
        self.putovanje = get_object_or_404(Putovanje, name=self.kwargs['putovanje'])
        return Prijave.objects.filter(putovanje=self.putovanje)
    

class PutovanjeDetailView(DetailView):
    model = Putovanje
    template_name = 'main/putovanje_detail.html'  
    context_object_name = 'putovanje' 

    def get_object(self):
        return get_object_or_404(Putovanje, putovanje_sifraPutovanja=self.kwargs['putovanje_sifraPutovanja'])

def homepage(request):
    return HttpResponse('Welcome to homepage! <strong>#samoOIRI</strong>')

def index(request):
    return render(request, 'main/index.html')

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
