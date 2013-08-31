""" Python Support """
# Not Applicable

""" Django Support """
from django.test import TestCase
from django.core.exceptions import ValidationError

""" Internal Support """
from Component.models import (Data, Export, Import, Procedure,
                              Metadata)
from Component.validators import (_validate_data, _validate_export,
    _validate_import, _validate_metadata, _validate_procedure)


"""
 Component/tests.py
 
 Author(s)   : Matthew J Swann     
 Version     : 1.0
 Last Update : 2013-08-31
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
    def test_validator_10_00_00_data(self):
        current = Data.objects.create(
                    data_id = '0400 4000',              
                        )
        try:
            _validate_data(current)
        except ValidationError:
            self.fail('failed to validate data')


    """
     {
      GENERAL PACKAGE FUNCTIONS
     }
     """#BLOCK: General Package Functions
    def test_general_package_00_00_00_get_x_y_z(self):
        pass    
