from django.contrib import admin
from studentapp.models import studentModel
# Register your models here.

class studentAdmin(admin.ModelAdmin):
    list_display = ['name','email','phone','roll']
    list_display_links = ['phone']
    
admin.site.register(studentModel,studentAdmin)