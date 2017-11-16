from django.contrib import admin

from .models import *

admin.site.register(User)
admin.site.register(Plant)
admin.site.register(HMeasure)
admin.site.register(TMeasure)


