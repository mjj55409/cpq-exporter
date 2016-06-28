from django.contrib import admin

from .models import Repository, KB, Destination, DatabaseDestination, SAPDestination

admin.site.register(Repository)
admin.site.register(KB)
admin.site.register(Destination)
admin.site.register(DatabaseDestination)
admin.site.register(SAPDestination)
