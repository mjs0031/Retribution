""" Python Support """
# Not Applicable

""" Django Support """
from django.contrib import admin

""" Internal Support """
# Not Applicable


"""
 Control/admin.py
 
 Author(s)   : Matthew J Swann     
 Version     : 1.0
 Last Update : 2013-08-12
 Update by   : Matthew J Swann
 
 This code imports each database table from each internal support
  package and then registers these to the admin site.
  
  DO NOT USE: import *
  This will import every support package within each models.py file.
"""


"""
 {
  Component
 }
 """#BLOCK: Component
class DataAdmin(admin.ModelAdmin):
    list_display  = ('id', 'data_id', 'data_tag', 'topic', 'last_modified')
    list_filter   = ('topic',)
    search_fields = ['last_modified', 'data_id', 'data_tag']
    ordering      = ['data_id', 'topic', 'last_modified']
    fieldsets     = (               
        ( 'Advanced options', {
            'classes': ('wide', 'extrapretty'),
            'fields' : ('data_id', 'data_tag', 'topic', 'last_modified', 
                        'description', 'calling_functions')
                 }),) 


class ExportAdmin(admin.ModelAdmin):
    list_display  = ('id', 'export_id', 'export_tag', 'last_modified')
    search_fields = ['last_modified', 'export_id', 'export_tag']
    ordering      = ['export_id', 'export_tag']
    fieldsets     = (               
        ( 'Advanced options', {
            'classes': ('wide', 'extrapretty'),
            'fields' : ('export_id', 'export_tag', 'description', 'last_modified')
                 }),)


class ImportAdmin(admin.ModelAdmin):
    list_display  = ('id', 'import_id', 'import_tag', 'library', 'last_modified')
    search_fields = ['last_modified', 'import_id', 'import_tag', 'library']
    ordering      = ['import_id', 'import_tag']
    fieldsets     = (               
        ( 'Advanced options', {
            'classes': ('wide', 'extrapretty'),
            'fields' : ('import_id', 'import_tag', 'library', 
                        'description', 'last_modified')
                 }),)


class MetadataAdmin(admin.ModelAdmin):
    list_display  = ('id', 'component', 'encrypted', 'self_modifying')
    list_filter   = ('encrypted', 'self_modifying', 'self_mod_contained_to_self')
    search_fields = ['last_modified', 'component']
    ordering      = ['component', ]
    fieldsets     = (               
        ( 'Advanced options', {
            'classes': ('wide', 'extrapretty'),
            'fields' : ('component', 'encrypted', 'self_modifying', 'self_mod_contained_to_self', 
                        'encryption_type', 'last_modified')
                 }),)


class ProcedureAdmin(admin.ModelAdmin):
    list_display  = ('id', 'routine_id', 'routine_tag', 'topic', 'last_modified')
    list_filter   = ('topic',)
    search_fields = ['last_modified', 'routine_id', 'routine_tag']
    ordering      = ['routine_id', 'topic', 'last_modified']
    fieldsets     = (               
        ( 'Advanced options', {
            'classes': ('wide', 'extrapretty'),
            'fields' : ('routine_id', 'routine_tag', 'topic', 'last_modified', 
                        'description', 'calling_functions', 'called_functions')
                 }),) 
    
from Component.models import (
                    Data,
                    Export,
                    Import,
                    Metadata,
                    Procedure
                        )
admin.site.register(Data, DataAdmin)
admin.site.register(Export, ExportAdmin)
admin.site.register(Import, ImportAdmin)
admin.site.register(Metadata, MetadataAdmin)
admin.site.register(Procedure, ProcedureAdmin)


"""
 {
  LOGIN_REGISTRATION
 }
 """# BLOCK: Login_Registration
class ProfileAdmin(admin.ModelAdmin):
    list_display  = ('id', '__unicode__', 'user', 'city', 'state', 'is_registered')
    list_filter   = ('is_registered', 'state')
    search_fields = ('city', 'state') 
    fieldsets     = (               
        ( 'Advanced options', {
            'classes': ('wide', 'extrapretty'),
            'fields' : ('user', 'addressLineOne', 'addressLineTwo', 'city',
                        'state', 'zipCode', 'phone', 'is_registered', 'activation_key', 
                        'avatar', 'date_initialized'),
                 }),)

from Login_Registration.models import (
                     Profile                   
                        )

admin.site.register(Profile, ProfileAdmin)


"""
 {
  Project
 }
 """#BLOCK: Project
class ProjectAdmin(admin.ModelAdmin):
    list_display  = ('id', 'project_name', 'initialization_date', 'last_modified')
    search_fields = ['last_modified', ]
    ordering      = ['last_modified', 'project_name']
    fieldsets     = (               
        ( 'Advanced options', {
            'classes': ('wide', 'extrapretty'),
            'fields' : ('project_name', 'initialization_date', 'last_modified')
                 }),)
    
from Project.models import (
                Project
                    )

admin.site.register(Project, ProjectAdmin)

