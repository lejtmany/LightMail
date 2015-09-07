from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Email, Contact

admin.site.register(Email)
admin.site.register(Contact)
