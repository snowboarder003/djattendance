from django.contrib import admin
from leaveslips.models import LeaveSlip, IndividualSlip, GroupSlip, MealOutSlip, NightOutSlip


# Register your models here.
admin.site.register(IndividualSlip)
admin.site.register(GroupSlip)
admin.site.register(MealOutSlip)
admin.site.register(NightOutSlip)
