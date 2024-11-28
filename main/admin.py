from django.contrib import admin
from .models import Putovanje
from .models import Prijave

## Register your models here.
admin.site.register(Putovanje)
admin.site.register(Prijave)
