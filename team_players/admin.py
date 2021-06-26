from django.contrib import admin
from .models import PlayersRequest,TeamsRequest
model=[PlayersRequest,TeamsRequest]	
admin.site.register(model)

