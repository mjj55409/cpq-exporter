from django.contrib import admin

from .models import KB, Destination, DatabaseDestination, SAPDestination, Project, Step

admin.site.register(KB)
admin.site.register(DatabaseDestination)
admin.site.register(SAPDestination)
admin.site.register(Destination)
admin.site.register(Project)
admin.site.register(Step)
