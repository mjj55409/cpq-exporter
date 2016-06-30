from django.contrib import admin

from .models import KB, Destination, DatabaseDestination, SAPDestination, Project, ProjectStep, Execution


admin.site.register(KB)
admin.site.register(DatabaseDestination)
admin.site.register(SAPDestination)
admin.site.register(Destination)
admin.site.register(Project)
admin.site.register(ProjectStep)
admin.site.register(Execution)
