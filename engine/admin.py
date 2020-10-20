from django.contrib import admin
from .models import Topic, Subject, Book, Tag
from django.contrib.admin.helpers import ActionForm
from django import forms
from django.contrib import messages

# Register your models here.


def approve_tags(modeladmin, request, queryset):
    queryset.update(approved=True)
    approve_tags.short_description = "Approve selected tags"


def disapprove_tags(modeladmin, request, queryset):
    queryset.update(approved=True)
    approve_tags.short_description = "Delete selected tags"


class UnsafeTag(Tag):
    class Meta:
        proxy = True


class UnsafeTagAdmin(admin.ModelAdmin):

    list_display = ['text', 'approved', 'create_date']
    list_filter = ['create_date']
    actions = [approve_tags, disapprove_tags]


class TagAdmin(admin.ModelAdmin):

    list_display = ['text', 'approved', 'create_date']
    list_filter = ['create_date']
    actions = [approve_tags, disapprove_tags]

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

class TopicAdmin(admin.ModelAdmin):
    actions = ['really_delete_selected']

    def get_actions(self, request):
        actions = super().get_actions(request)
        del actions['delete_selected']
        return actions

    def really_delete_selected(self, request, queryset):
        for obj in queryset:
            obj.delete()

        if queryset.count() == 1:
            message_bit = "1 topic entry was"
        else:
            message_bit = "%s topic entries were" % queryset.count()
        self.message_user(request, "%s successfully deleted." % message_bit)
    really_delete_selected.short_description = "Delete selected entries"


class BookAdmin(admin.ModelAdmin):
    actions = ['really_delete_selected']

    def get_actions(self, request):
        actions = super().get_actions(request)
        del actions['delete_selected']
        return actions

    def really_delete_selected(self, request, queryset):
        for obj in queryset:
            obj.delete()

        if queryset.count() == 1:
            message_bit = "1 book entry was"
        else:
            message_bit = "%s book entries were" % queryset.count()
        self.message_user(request, "%s successfully deleted." % message_bit)
    really_delete_selected.short_description = "Delete selected entries"


admin.site.register(Subject)
admin.site.register(Book, BookAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(UnsafeTag, UnsafeTagAdmin)
admin.site.register(Topic, TopicAdmin)
