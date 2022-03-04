from django.contrib import admin
from .models import Dweet, Profile
from django.contrib.auth.models import Group, User
# Register your models here.


class ProfileInline(admin.StackedInline):
    model = Profile

class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ['username']
    inlines = [ProfileInline]




admin.site.unregister(Group)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Dweet)

#admin.site.register(Profile)
