from django.contrib import admin
from demo_app.models import *

# Register your models here.



class MasterAdmin(admin.ModelAdmin):
    list_display=['created_user','created_date','is_active']
    def save_model(self, request,obj,form, change):
        obj.created_user=request.user
        super().save_model(request, obj, form, change)


class StateAdmin(MasterAdmin):
    list_display=['statename','created_user','created_date']
    exclude=['created_user']

admin.site.register(New_State,StateAdmin)

class DistrictAdmin(MasterAdmin):
    list_display=['districtname','state','created_date']
    exclude=['created_user']

admin.site.register(District,DistrictAdmin)
class Student_genderAdmin(MasterAdmin):
    list_display=['StudentName','student_details','created_date']
    exclude=['created_user']

admin.site.register(Student_gender,Student_genderAdmin)
