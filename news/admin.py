from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from django import forms
from .models import News, Category


class NewsAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = News
        fields = "__all__"


class NewsAdmin(admin.ModelAdmin):
    form = NewsAdminForm
    list_display = ("id", "title", "category", "author", "created_at", "updated_at", "is_published")
    list_display_links = ("id", "title", "author")
    search_fields = ("title", "content")
    list_editable = ("is_published",)
    list_filter = ("is_published", "category", "author")


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    list_display_links = ("id", "title")
    search_fields = ("title",)


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
