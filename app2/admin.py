from django.contrib import admin
from .models import TodoModel
# Register your models here.
class TodoAdmin(admin.ModelAdmin):
    list_display=["name","subject","activity"]
admin.site.register(TodoModel,TodoAdmin)    