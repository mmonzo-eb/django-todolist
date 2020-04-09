from django.contrib import admin
from .models import (
    Priority,
    Todo,
)


class PriorityAdmin(admin.ModelAdmin):
    list_display = ('name', 'order',)
# Register your models here.


admin.site.register(Priority, PriorityAdmin)
admin.site.register(Todo)
