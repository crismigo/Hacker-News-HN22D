from django.contrib import admin
from .models import SubmissionType, Submission, Vote, ActionType, Comment


# Register your models here.
class SubmissionTypeAdmin(admin.ModelAdmin):
    readonly_fields = ["created_at"]


class SubmissionAdmin(admin.ModelAdmin):
    readonly_fields = ["created_at"]

class VoteAdmin(admin.ModelAdmin):
    readonly_fields = ["created_at"]

class ActionTypeAdmin(admin.ModelAdmin):
    readonly_fields = ["created_at"]

class CommentAdmin(admin.ModelAdmin):
    readonly_fields = ["created_at"]

admin.site.register(Submission, SubmissionAdmin)
admin.site.register(SubmissionType, SubmissionTypeAdmin)

admin.site.register(Vote, VoteAdmin)

admin.site.register(ActionType, ActionTypeAdmin)
admin.site.register(Comment, CommentAdmin)
