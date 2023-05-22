from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import Cart, Favorite, Ingredient, Recipe, RecipeIngredient, Tag


class AmountIngredientAdmin(admin.TabularInline):
    model = RecipeIngredient
    fields = ('ingredient', 'measurement_unit', 'amount')
    readonly_fields = ('measurement_unit', )
    extra = 0

    def measurement_unit(self, obj):
        return obj.ingredient.measurement_unit
    measurement_unit.short_description = 'еденица измерения'


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'name', 'count_favorites')
    list_filter = ('author', 'name', 'tags')
    inlines = [AmountIngredientAdmin, ]

    def count_favorites(self, obj):
        return obj.favorites.count()


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'color')


@admin.register(Ingredient)
class IngredientAdmin(ImportExportModelAdmin):
    list_display = ('name', 'measurement_unit')
    list_filter = ('name',)


admin.site.register(Favorite)
admin.site.register(Cart)
