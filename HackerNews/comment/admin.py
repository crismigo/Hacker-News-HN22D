from django.contrib import admin
from .models import ActionType, Comment


# Register your models here.
class ActionTypeAdmin(admin.ModelAdmin):
    readonly_fields = ["created_at"]


class CommentAdmin(admin.ModelAdmin):
    readonly_fields = ["created_at"]


admin.site.register(ActionType, ActionTypeAdmin)
admin.site.register(Comment, CommentAdmin)
