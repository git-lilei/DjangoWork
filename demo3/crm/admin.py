from django.contrib import admin
from .models import Users,Roles,Modules,UserRoles,RoleModules
# Register your models here.
admin.site.register(Users)
admin.site.register(Roles)
admin.site.register(Modules)
admin.site.register(UserRoles)
admin.site.register(RoleModules)