""" Python Support """
# Not Applicable

""" Django Support """
from django.test import TestCase

""" Internal Support """
# Not Applicable


"""
 Procedures/tests.py
 
 Author(s)   :      
 Version     : 1.0
 Last Update : 2013-07-28
 Update by   : Matthew J Swann

 
     All tests being with 'test' and are followed by table name.
     
     First number section is for function block tagging.
     Second number section is for test number within block.
     Third number is for happy/sad path testing.
     
     All tests end explicitly with block tag name matching function. 
 
"""

class Test(TestCase):
    fixtures = [
                #'Testing/fixtures/procedure_testdata.json',
                #    
                ]

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
    def test_validator_00_00_00_get_x_y_z(self):
        pass 


    """
     {
      GENERAL PACKAGE FUNCTIONS
     }
     """#BLOCK: General Package Functions
    def test_general_package_00_00_00_get_x_y_z(self):
        pass    
