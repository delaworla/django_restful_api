from django.contrib import admin
from .models import Customer
# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('title', 'full_name','gender', 'status', 'created_by', 'time_created',)
    readonly_fields = ('time_created', )

    def full_name(self, obj):
        return obj.first_name + " " +obj.last_name

admin.site.register(Customer,CustomerAdmin)