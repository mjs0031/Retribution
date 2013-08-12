""" Python Package Support """
# Not Applicable

""" Django Package Support """
# Not Applicable

""" Internal imports """
# INLINE IMPORTS --> Circular dependency avoidance when syncing DB


"""

 Procedure/validators.py
 
 Author(s)   : Matthew J Swann     
 Version     : 1.0
 Last Update : 2013-07-30
 Update by   : Matthew J Swann
 
"""

def _validate_procedure( procedure ):
    """
    Validate a procedure object AS a procedure object.
    
    @param procedure : Procedure object
    @raise TypeError : Raise if param not of type Procedure
    @return { procedure } : Returns validated object
    """
    from Procedure.models import Procedure
    
    if not isinstance(procedure, Procedure):
        raise TypeError('_validate_procedure() requires param of Procedure Type')
    
    return procedure
