from django.contrib import admin
from .models import Fcuser

# Register your models here.


class fcuseradmin(admin.ModelAdmin):
    list_display = ('username', 'password', 'useremail', 'registered_dttm')


admin.site.register(Fcuser, fcuseradmin)
