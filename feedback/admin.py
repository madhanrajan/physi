from django.contrib import admin
from .models import FeedbackData


class FeedbackAdmin(admin.ModelAdmin):

    list_display = ['data', 'create_date']
    list_filter = ['create_date']


# Register your models here.
admin.site.register(FeedbackData, FeedbackAdmin)
