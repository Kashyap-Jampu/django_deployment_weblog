from django.contrib import admin
from .models import category,Post,comment

# Register your models here.
class postadmin(admin.ModelAdmin):
    list_display=('title','is_published','posted_at')
    list_filter=('is_published','posted_at')
    list_editable=['is_published']

class commentadmin(admin.ModelAdmin):
    list_display=('namee','is_resolved','commented_at')
    list_filter=('commented_at','is_resolved')
    list_editable=['is_resolved']

admin.site.register(category)
admin.site.register(Post,postadmin)
admin.site.register(comment,commentadmin)
