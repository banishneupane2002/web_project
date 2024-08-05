from django.contrib import admin


from .models import UserForm

@admin.register(UserForm)
class UserFormAdmin(admin.ModelAdmin):
    list_display = ('name', 'sex', 'country', 'message', 'newsletter')
    search_fields = ('name', 'sex', 'country')