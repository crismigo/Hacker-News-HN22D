from django.contrib import admin

# Register your models here.
from .models import Submission, SubmissionType


class SubmissionTypeAdmin(admin.ModelAdmin):
    readonly_fields = ["created_at"]


class SubmissionAdmin(admin.ModelAdmin):
    readonly_fields = ["created_at"]

admin.site.register(Submission, SubmissionAdmin)
admin.site.register(SubmissionType, SubmissionTypeAdmin)