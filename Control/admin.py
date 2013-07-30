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
 Last Update : 2013-07-30
 Update by   : Matthew J Swann
 
 This code imports each database table from each internal support
  package and then registers these to the admin site.
  
  DO NOT USE: import *
  This will import every support package within each models.py file.
"""


"""
 {
  Data
 }
 """#BLOCK: Data
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
    
from Data.models import (
                    Data
                        )

admin.site.register(Data, DataAdmin)


"""
 {
  Procedures
 }
 """#BLOCK: Procedures
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
    
from Procedure.models import (
                    Procedure
                        )

admin.site.register(Procedure, ProcedureAdmin)
