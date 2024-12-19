from django.contrib import admin
from .models import Putovanje
from .models import Prijave
from main.models import *

## Register your models here.

models_list = [Putovanje, Prijave]

## Register your models here.
admin.site.register(models_list)
