from django.contrib import admin
from .models import Vote


# Register your models here.
class VoteAdmin(admin.ModelAdmin):
    readonly_fields = ["created_at"]


admin.site.register(Vote, VoteAdmin)
