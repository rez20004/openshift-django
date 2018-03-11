from django.contrib import admin

from universities.models import Universities


class UniversitiesViewAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'website', 'founded']


admin.site.register(Universities, UniversitiesViewAdmin)
