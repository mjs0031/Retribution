""" Python Support """
# Not Applicable

""" Django Support """
from django.test import TestCase
from django.core.exceptions import ValidationError

""" Internal Support """
from Component.models import (Data,      create_data, 
                              Export,    create_export, 
                              Import,    create_import,
                              Procedure, create_procedure,
                              Metadata,  create_metadata)
from Component.validators import (_validate_data, _validate_export,
    _validate_import, _validate_metadata, _validate_procedure)


"""
 Component/tests.py
 
 Author(s)   : Matthew J Swann     
 Version     : 1.0
 Last Update : 2013-09-11
 Update by   : Matthew J Swann

 
     All tests being with 'test' and are followed by table name.
     
     First number section is for function block tagging.
     Second number section is for test number within block.
     Third number is for happy/sad path testing.
     
     All tests end explicitly with block tag name matching function. 
 
"""

class Test(TestCase):
    #fixtures = [
                #'Testing/fixtures/procedure_testdata.json',
                #'Testing/fixtures/data_testdata.json',    
    #            ]


    """
     {
      DATA
     }
     """#BLOCK: Data
    def test_data_00_00_00_get_x_y_z(self):
        pass


    """
     {
      EXPORT
     }
     """#BLOCK: Export
    def test_export_00_00_00_get_x_y_z(self):
        pass


    """
     {
      IMPORT
     }
     """#BLOCK: Import
    def test_import_00_00_00_get_x_y_z(self):
        pass


    """
     {
      METADATA
     }
     """#BLOCK: Metadata
    def test_metadata_00_00_00_get_x_y_z(self):
        pass


    """
     {
      PROCEDURE
     }
     """#BLOCK: Procedure
    def test_procedure_00_00_00_get_x_y_z(self):
        pass 


    """
     {
      VALIDATORS
     }
     """#BLOCK: Validators
    def test_validator_10_01_00_data(self):
        current = Data.objects.create(
                    data_id = '0400 4000',              
                        )
        try:
            _validate_data(current)
        except ValidationError:
            self.fail('failed to validate data')
            

    def test_validator_10_02_00_import(self):
        current = Import.objects.create(
                    import_id = '0400 4000',              
                        )
        try:
            _validate_import(current)
        except ValidationError:
            self.fail('failed to validate import')
            
            
    def test_validator_10_03_00_export(self):
        current = Export.objects.create(
                    export_id = '0400 4000',              
                        )
        try:
            _validate_export(current)
        except ValidationError:
            self.fail('failed to validate export')
            

    def test_validator_10_04_00_metadata(self):
        current = Metadata.objects.create(
                    component = 'E-1',              
                        )
        try:
            _validate_metadata(current)
        except ValidationError:
            self.fail('failed to validate metadata')
            
            
    def test_validator_10_05_00_procedure(self):
        current = Procedure.objects.create(
                    routine_id = '0400 4000',               
                        )
        try:
            _validate_procedure(current)
        except ValidationError:
            self.fail('failed to validate procedure')


    """
     {
      GENERAL PACKAGE FUNCTIONS
     }
     """#BLOCK: General Package Functions
    def test_general_package_10_01_00_get_create_data(self):
        # Battery One
        current = create_data(data_id='0400 4000')
        self.assertEquals('0400 4000', current.data_id)
        self.assertEquals(u'',         current.data_tag)
        self.assertEquals(u'',         current.size)
        self.assertEquals(u'U',        current.topic)
        self.assertEquals('',          current.description)
        self.assertEquals(str,         type(current.data_tag))
        self.assertEquals(str,         type(current.size))
        self.assertEquals(str,         type(current.topic))
        self.assertEquals(str,         type(current.description))   
        # Battery Two
        current = create_data(data_id     ='0400 4001',
                              data_tag    ='string array',
                              size        = 'X',
                              topic       = 'U',
                              description ='Hacking mechanism')
        self.assertEquals('0400 4001',         current.data_id)
        self.assertEquals('string array',      current.data_tag)
        self.assertEquals('X',                 current.size)
        self.assertEquals(u'U',                current.topic)
        self.assertEquals('Hacking mechanism', current.description)
        self.assertEquals(str,                 type(current.data_tag))
        self.assertEquals(str,                 type(current.size))
        self.assertEquals(str,                 type(current.topic))
        self.assertEquals(str,                 type(current.description))   
    
    
    def test_general_package_10_02_00_get_create_export(self):
        # Battery One
        current = create_export(export_id='0400 4000')
        self.assertEquals('0400 4000', current.export_id)
        self.assertEquals(u'',         current.export_tag)
        self.assertEquals('',          current.description)
        self.assertEquals(str,         type(current.export_tag))
        self.assertEquals(str,         type(current.description))   
        # Battery Two
        current = create_export(export_id   ='0400 4001',
                                export_tag  ='string array',
                                description ='Hacking mechanism')
        self.assertEquals('0400 4001',         current.export_id)
        self.assertEquals('string array',      current.export_tag)
        self.assertEquals('Hacking mechanism', current.description)
        self.assertEquals(str,                 type(current.export_tag))
        self.assertEquals(str,                 type(current.description))   


    def test_general_package_10_03_00_get_create_import(self):
        # Battery One
        current = create_import(import_id='0400 4000')
        self.assertEquals('0400 4000', current.import_id)
        self.assertEquals(u'',         current.import_tag)
        self.assertEquals('',          current.library)
        self.assertEquals('',          current.description)
        self.assertEquals(str,         type(current.import_tag))
        self.assertEquals(str,         type(current.library))
        self.assertEquals(str,         type(current.description))   
        # Battery Two
        current = create_import(import_id   ='0400 4001',
                                import_tag  ='string array',
                                library     = 'MW384',
                                description ='Hacking mechanism')
        self.assertEquals('0400 4001',         current.import_id)
        self.assertEquals('string array',      current.import_tag)
        self.assertEquals('MW384',             current.library)
        self.assertEquals('Hacking mechanism', current.description)
        self.assertEquals(str,                 type(current.import_tag))
        self.assertEquals(str,                 type(current.library))
        self.assertEquals(str,                 type(current.description))   


    def test_general_package_10_04_00_get_create_metadata(self):
        # Battery One
        current = create_metadata(component='E-1')
        self.assertEquals('E-1', current.component)
        self.assertEquals(None,  current.encrypted)
        self.assertEquals(None,  current.self_modifying)
        self.assertEquals(None,  current.self_mod_contained_to_self)
        self.assertEquals(''  ,  current.encryption_type)
        # Battery Two
        current = create_metadata(component                  ='E-1',
                                  encrypted                  = False,
                                  self_modifying             = True,
                                  self_mod_contained_to_self = None,
                                  encryption_type            = 'reqs')
        self.assertEquals('E-1',  current.component)
        self.assertEquals(False,  current.encrypted)
        self.assertEquals(True,   current.self_modifying)
        self.assertEquals(None,   current.self_mod_contained_to_self)
        self.assertEquals('reqs', current.encryption_type)


    def test_general_package_10_05_00_get_create_procedure(self):
        # Battery One
        current = create_procedure(routine_id='0400 4000')
        self.assertEquals('0400 4000', current.routine_id)
        self.assertEquals(u'',         current.routine_tag)
        self.assertEquals('',          current.topic)
        self.assertEquals('',          current.description)
        self.assertEquals(str,         type(current.routine_tag))
        self.assertEquals(str,         type(current.library))
        self.assertEquals(str,         type(current.description))   
        # Battery Two
        current = create_procedure(routine_id  ='0400 4001',
                              routine_tag ='string array',
                              topic       = 'U',
                              description ='Hacking mechanism')
        self.assertEquals('0400 4001',         current.routine_id)
        self.assertEquals('string array',      current.routine_tag)
        self.assertEquals('U',             current.topic)
        self.assertEquals('Hacking mechanism', current.description)
        self.assertEquals(str,                 type(current.routine_tag))
        self.assertEquals(str,                 type(current.library))
        self.assertEquals(str,                 type(current.description))
    
