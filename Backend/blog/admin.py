from django.contrib import admin
from .models import Blog, Category
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    model = Category
    readonly_fields=('id',)


admin.site.register(Blog)
admin.site.register(Category, CategoryAdmin)
