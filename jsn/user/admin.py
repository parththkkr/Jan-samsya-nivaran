from django.contrib import admin

# Register your models here.
from user.models import Complaint
 

class ComplaintAdmin(admin.ModelAdmin):
    readonly_fields=('complaint_id','username','problem','description','image','address','zip','ward','date')
admin.site.register(Complaint,ComplaintAdmin)