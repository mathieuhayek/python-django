from django.contrib import admin



from .models import  Eleve, Event, Cour, Projet, Prof


class CourInline(admin.TabularInline):
    model = Cour.Eleves.through

class CourAdmin(admin.ModelAdmin):
    inlines = [
       CourInline,
    ]

class EleveAdmin(admin.ModelAdmin):
    inlines = [
        CourInline,
    ]

admin.site.register(Eleve, EleveAdmin)
admin.site.register(Event)
admin.site.register(Cour,CourAdmin)
admin.site.register(Projet)
admin.site.register(Prof)

 