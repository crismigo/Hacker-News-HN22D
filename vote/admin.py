from django.contrib import admin

# Register your models here.
from .models import Vote


class VoteAdmin(admin.ModelAdmin):
    readonly_fields = ["created_at"]

admin.site.register(Vote, VoteAdmin)