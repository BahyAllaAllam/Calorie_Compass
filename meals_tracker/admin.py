from django.contrib import admin
from meals_tracker.models import Meals
from meals_tracker.forms import MealForm


# Register your models here.


@admin.register(Meals)
class MealsAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'formatted_created_at', 'calories')
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ('created_at','calories',)

    def formatted_created_at(self, obj):
        return obj.created_at.strftime('%Y-%m-%d')

    formatted_created_at.admin_order_field = 'created_at'
    formatted_created_at.short_description = 'Created At'