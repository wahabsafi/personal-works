from django.contrib import admin
from .models import Complex,Block,Unit 
# from account.admin import FamilyInline
# Register your models here.


@admin.register(Complex)
class ComplexAdmin(admin.ModelAdmin):
    '''Admin View for Complex'''

    list_display = ("name","address")
    list_filter = ('name',)
    # inlines = [
    #     Inline,
    # ]
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    # search_fields = ('',)
    # date_hierarchy = ''
    # ordering = ('',)

@admin.register(Block)
class BlockAdmin(admin.ModelAdmin):
    '''Admin View for Block'''

    list_display = ('complex','no')
    list_filter = ('complex','no')
    # inlines = [
    # #     Inline,
    # ]
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    # search_fields = ('',)
    # date_hierarchy = ''
    # ordering = ('',)

@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    '''Admin View for Unit'''
    model=Unit
    list_display = ('owner','owner_family','phone','block','no',)
    list_filter = ('owner','block','no',)
    # inlines = [
    #     FamilyInline,
    # ]
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    # search_fields = ('',)
    # date_hierarchy = ''
    # ordering = ('',)


class UnitInline(admin.TabularInline):
    '''Admin View for Unit'''
    model=Unit
    # inlines = [
    #     Inline,
    # ]
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    # search_fields = ('',)
    # date_hierarchy = ''
    # ordering = ('',)