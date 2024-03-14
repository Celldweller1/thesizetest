from django.contrib import admin

from .models import *

class UserScanAdmin(admin.ModelAdmin):
    def has_change_permission(self, request, obj=None):
        return False
    list_display = ('name', 'email','age','contactNumber','gender','submitDate')
    list_filter = ('name', 'email','age','contactNumber','gender','submitDate')
class SystemConfigurationAdmin(admin.ModelAdmin):
    def has_delete_permission(self, request, obj=None):
        return False
    list_display = ('key', 'value')
    list_filter = ('key', 'value')
    readonly_fields = ('key',)
# Register your models here.
admin.site.register(UserScan,UserScanAdmin)
admin.site.register(SystemConfiguration,SystemConfigurationAdmin)