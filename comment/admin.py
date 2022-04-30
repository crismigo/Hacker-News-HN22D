from django.contrib import admin

# Register your models here.
from .models import Comment, ActionType


class CommentAdmin(admin.ModelAdmin):
    readonly_fields = ["created_at"]

class ActionTypeAdmin(admin.ModelAdmin):
    readonly_fields = ["created_at"]


admin.site.register(ActionType, ActionTypeAdmin)
admin.site.register(Comment, CommentAdmin)
