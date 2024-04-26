from django.contrib import admin
from userauths.models import User, Profile
from import_export.admin import ImportExportModelAdmin


# class ProfileAdmin(admin.ModelAdmin):
class ProfileAdmin(ImportExportModelAdmin):
    list_display = ['user', 'full_name', 'date']
    search_fields = ['full_name']

class UserAdmin(ImportExportModelAdmin):
    pass

admin.site.register(User, UserAdmin)
admin.site.register(Profile, ProfileAdmin)
