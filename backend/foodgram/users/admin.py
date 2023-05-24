from django.contrib import admin

from .models import Follow, User


class UserAdmin(admin.ModelAdmin):
    list_display = ("email", "username",)
    list_filter = ("email", "username",)
    empty_value_display = "-пусто-",


admin.site.register(Follow)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
