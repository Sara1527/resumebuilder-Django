from django.contrib import admin
from . models import Resume


# Register your models here.
class ResumeAdmin(admin.ModelAdmin):
    list_display =['name','phone','email','experience','banner']

admin.site.register(Resume,ResumeAdmin)
