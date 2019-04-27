from django.contrib import admin
from testapp.models import hydjobs, bangalorejobs, chennaijobs, punejobs

# Register your models here.
class hydjobsadmin(admin.ModelAdmin):
    list_display = ['date', 'company', 'title', 'eligibility', 'address', 'email', 'phonenumber']

class bangalorejobsadmin(admin.ModelAdmin):
    list_display = ['date', 'company', 'title', 'eligibility', 'address', 'email', 'phonenumber']

class chennaijobsadmin(admin.ModelAdmin):
    list_display = ['date', 'company', 'title', 'eligibility', 'address', 'email', 'phonenumber']

class punejobsadmin(admin.ModelAdmin):
    list_display = ['date', 'company', 'title', 'eligibility', 'address', 'email', 'phonenumber']

admin.site.register(hydjobs,hydjobsadmin)
admin.site.register(chennaijobs, chennaijobsadmin)
admin.site.register(punejobs, punejobsadmin)
admin.site.register(bangalorejobs, bangalorejobsadmin)
