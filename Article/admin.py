from django.contrib import admin
from .models import Post , Static
# Register your models here.

class Articlestatic(admin.ModelAdmin):
    list_display = ('title' , 'status',)


admin.site.register(Post , Articlestatic)
admin.site.register(Static)