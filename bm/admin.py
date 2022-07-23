from django.contrib import admin
from .models import Appointment, Package, Category, Team, Gallery


admin.site.register(Appointment)
admin.site.register(Package)
admin.site.register(Category)
admin.site.register(Team)
admin.site.register(Gallery)

