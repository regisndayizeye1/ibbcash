from django.contrib import admin
from transfers.models import *


class TarifAdmin(admin.ModelAdmin):
    list_display = ('limit_inferior', 'limit_superior', 'montant')
    search_fields = ('montant',)
    ordering = ('montant',)

class TransferAdmin(admin.ModelAdmin):
    list_display = ('last_namesender', 'first_namesender', 'montant','last_namereceiver','first_namereceiver')
    search_fields = ('montant',)
    ordering = ('montant',)

admin.site.register(Tarif, TarifAdmin)
admin.site.register(Transfert,TransferAdmin)


