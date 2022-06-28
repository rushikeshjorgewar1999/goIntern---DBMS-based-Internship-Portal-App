from django.contrib import admin
from registration.models import company_register,intern_register
# Register your models here.

admin.site.register((company_register,intern_register))


