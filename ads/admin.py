from django.contrib import admin
from ads.models.exchange_proposals import ExchangeProposal
from ads.models.ads import Ad

# Register your models here.

admin.site.register(Ad)
admin.site.register(ExchangeProposal)
