from django.contrib import admin

from people.models import Person, Quote

class PersonAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['person_name','slug','wiki']}),
        ('Date information', {'fields': ['pub_date','updated_date'], 'classes': ['collapse']}),
    ]
admin.site.register(Person, PersonAdmin)


class QuoteAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['quote_text','slug','source', 'topics', 'person', 'date']}),
        ('Date information', {'fields': ['pub_date','updated_date'], 'classes': ['collapse']}),
    ]
admin.site.register(Quote, QuoteAdmin)
