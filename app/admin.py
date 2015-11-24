from django.contrib import admin
from .models import server_func_categ, server_app_categ, server_list, module_list

# Register your models here.

admin.site.register(server_func_categ)
admin.site.register(server_app_categ)

class Servers(admin.ModelAdmin):
    #admin list
    fieldsets = [
            (None,  {'fields': ['server_name']}),
            ('IP Information', {'fields': ['server_ip', 'server_eip']}),
            ('Opera System', {'fields': ['server_op']}),
            ('Date Information', {'fields': ['create_date'], 'classes': ['collapse']})
    ]

    list_display = ('server_name', 'server_ip', 'server_eip', 'server_op', 'create_date')
    #sort list
    list_filter = ['create_date']
    #search list
    search_fields = ['server_name', 'server_ip', 'server_eip']

admin.site.register(server_list, Servers)

admin.site.register(module_list)
