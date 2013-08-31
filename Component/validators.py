""" Python Package Support """
# Not Applicable

""" Django Package Support """
from django.core.exceptions import ValidationError

""" Internal imports """
# Not Applicable

"""

 Component/validators.py
 
 Author(s)   : Matthew J Swann     
 Version     : 1.0
 Last Update : 2013-08-31
 Update by   : Matthew J Swann
 
"""

#BLOCK: Pure Validators
def _validate_data( data ):
    """
    Validate a data object AS a data object.
    
    @param data      : Data object
    @raise TypeError : Raise if param not of type Data
    @return { data } : Returns validated object
    """
    from Component.models import Data
    
    if not isinstance(data, Data):
        raise TypeError('_validate_data() requires param of Data Type')
    
    return data


def _validate_import( import_object ):
    """
    Validate an import object AS an import object.
    
    @param import_obvject : Import object
    @raise TypeError      : Raise if param not of type Import
    @return { import }    : Returns validated object
    """
    from Component.models import Import
    
    if not isinstance(import_object, Import):
        raise TypeError('_validate_import() requires param of Import Type')
    
    return import_object


def _validate_export( export_object ):
    """
    Validate an export object AS an export object.
    
    @param edport_object : Import object
    @raise TypeError     : Raise if param not of type Export
    @return { export }   : Returns validated object
    """
    from Component.models import Export
    
    if not isinstance(export_object, Export):
        raise TypeError('_validate_export() requires param of Export Type')
    
    return export_object


def _validate_metadata( metadata ):
    """
    Validate a metadata object AS a metadata object.
    
    @param metadata      : Metadata object
    @raise TypeError     : Raise if param not of type Metadata
    @return { metadata } : Returns validated object
    """
    from Component.models import Metadata
    
    if not isinstance(metadata, Metadata):
        raise TypeError('_validate_metadata() requires param of Metadata Type')
    
    return metadata


def _validate_procedure( procedure ):
    """
    Validate a procedure object AS a procedure object.
    
    @param procedure      : Procedure object
    @raise TypeError      : Raise if param not of type Procedure
    @return { procedure } : Returns validated object
    """
    from Component.models import Procedure
    
    if not isinstance(procedure, Procedure):
        raise TypeError('_validate_procedure() requires param of Procedure Type')
    
    return procedure


#BLOCK: Polymorphic Tag Logic
def produce_component_tag( component ):
    """
    Produces unique polymorphic tag for a component in char/str format
    
    @param component : Unvalidated component type
    
    @raise TypeError     : If passed parameter is not of component type
    @return { char/str } : Representation of the object in char/str format.
    """
    # TO BE FINISHED VIA TD_DB_D
    
    
def process_component_tag( target ):
    """
    Processes a unique polymorphic tag for a component and returns the object
    
    @param target : Unvalidated char/str representation of a component object
    
    @raise TypeError      : If passed target is not of transmogrifiable type
    @return { component } : Object represented by the tag 
    """
    # TO BE FINISHED VIA TD_DB_D
    
    