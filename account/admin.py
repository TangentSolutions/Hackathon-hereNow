from django.contrib import admin

from account.models import UserDetail, UserRole


class UserDetailAdmin(admin.ModelAdmin):
    model = UserDetail


class UserRoleAdmin(admin.ModelAdmin):
    model = UserRole

admin.site.register(UserDetail, UserDetailAdmin)
admin.site.register(UserRole, UserRoleAdmin)