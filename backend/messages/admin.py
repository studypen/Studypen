from django.contrib import admin
from . import models


@admin.register(models.Message)
class MsgAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ClassMessage)
class ClassMsgAdmin(admin.ModelAdmin):
    pass
