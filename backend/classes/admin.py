from django.contrib import admin
from . import models


@admin.register(models.Invites)
class InvitesAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Classes)
class ClassAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ResheduleTime)
class ResheduleTimeAdmin(admin.ModelAdmin):
    pass


@admin.register(models.SheduleTime)
class SheduleTimeAdmin(admin.ModelAdmin):
    pass
