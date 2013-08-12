""" Python Package Support """
# Not Applicable

""" Django Package Support """
# Not Applicable

""" Internal imports """
# INLINE IMPORTS --> Circular dependency avoidance when syncing DB


"""

 Data/validators.py
 
 Author(s)   : Matthew J Swann     
 Version     : 1.0
 Last Update : 2013-07-30
 Update by   : Matthew J Swann
 
"""

def _validate_data( data ):
    """
    Validate a data object AS a data object.
    
    @param data      : Data object
    @raise TypeError : Raise if param not of type Data
    @return { data } : Returns validated object
    """
    from Data.models import Data
    
    if not isinstance(data, Data):
        raise TypeError('_validate_data() requires param of Data Type')
    
    return data
