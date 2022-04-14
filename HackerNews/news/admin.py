from django.contrib import admin
from .models import SubmissionType, Submission


# Register your models here.
class SubmissionTypeAdmin(admin.ModelAdmin):
    readonly_fields = ["created_at"]


class SubmissionAdmin(admin.ModelAdmin):
    readonly_fields = ["created_at"]


admin.site.register(Submission, SubmissionAdmin)
admin.site.register(SubmissionType, SubmissionTypeAdmin)
