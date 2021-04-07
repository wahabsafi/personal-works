# from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from account.admin import UserAdmin,UserInline
from .models import Family,Father,Mother,Person


class FatherInline(admin.TabularInline):
    '''Tabular Inline View for Father'''

    model = Father
    min_num = 0
    max_num = 20
    extra = 1
    # raw_id_fields = (,)
class MotherInline(admin.TabularInline):
    '''Tabular Inline View for Mother'''

    model = Mother
    min_num = 0
    max_num = 20
    extra = 1
    # raw_id_fields = (,)

@admin.register(Father)
class FatherAdmin(UserAdmin):
    '''Admin View for Father'''

    list_display = ('username','first_name','last_name','role',)
    list_filter = ('first_name',)
    # inlines = [
    #     Inline,
    # ]
    # raw_id_fields = ('',)
    readonly_fields = ('role','gender')
    
    # search_fields = ('',)
    # date_hierarchy = ''
    # ordering = ('',)

@admin.register(Mother)
class MotherAdmin(UserAdmin):
    '''Admin View for Mother'''
    list_display = ('username','first_name','last_name','role',)
    list_filter = ('first_name',)
    
    # inlines = [
    #     Inline,
    # ]
    # raw_id_fields = ('',)
    readonly_fields = ('role','gender')
    # search_fields = ('',)
    # date_hierarchy = ''
    # ordering = ('',)

@admin.register(Family)
class FamilyAdmin(admin.ModelAdmin):
    '''Admin View for Family'''
    model=Family
    # list_display = ('',)
    # list_filter = ('',)
    inlines = [
        UserInline,
    ]
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    # search_fields = ('',)
    # date_hierarchy = ''
    # ordering = ('',)

class FamilyInline(admin.TabularInline):
    '''Tabular Inline View for Family'''

    model = Family
    min_num = 1
    max_num = 20
    extra = 1
    # raw_id_fields = (,)
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    '''Admin View for Person'''
    model=Person
    # list_display = ('',)
    # list_filter = ('',)
    # inlines = [
    #     Inline,
    # ]
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    # search_fields = ('',)
    # date_hierarchy = ''
    # ordering = ('',)