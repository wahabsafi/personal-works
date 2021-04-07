from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from complex.admin import UnitInline
from django.utils.translation import gettext_lazy as _




@admin.register(User)
class UserAdmin(UserAdmin):
    '''Admin View for User'''
    fieldsets = (
        (_('User info'), {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'gender','birth_day','family','role','phone','email',)}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser','is_owner', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    list_display = ("username","first_name","last_name","phone","email","is_owner","is_staff","is_active")
    list_filter = ("first_name","last_name",)
    inlines = [
       
    ]
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    # search_fields = ('',)
    # date_hierarchy = ''
    # ordering = ('',)



class UserInline(admin.StackedInline):
    '''Tabular Inline View for User'''
    fieldsets = UserAdmin.fieldsets
    model = User
    min_num = 0
    max_num = 20
    extra = 1
    # raw_id_fields = (,)