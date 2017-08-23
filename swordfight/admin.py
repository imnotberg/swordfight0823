from django.contrib import admin
from .models import Game, Pick, League, Week, Season, Team, Comment

# Register your models here.

admin.site.register(League)
admin.site.register(Season)
admin.site.register(Week)
admin.site.register(Team)
admin.site.register(Game)
admin.site.register(Pick)
admin.site.register(Comment)
