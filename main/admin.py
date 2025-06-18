from django.contrib import admin
from .models import Pet, PetImage, Adoption

class PetImageInline(admin.TabularInline):
    model = PetImage
    extra = 1

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'breed', 'age', 'adopted')
    inlines = [PetImageInline]
    search_fields = ('name', 'breed')
    list_filter = ('adopted', 'breed')

@admin.register(Adoption)
class AdoptionAdmin(admin.ModelAdmin):
    list_display = ('adopter_name', 'pet', 'date')
    search_fields = ('adopter_name', 'pet__name')
