""" Python Support """
from datetime import datetime

""" Django Support """
from django.core.exceptions import ValidationError
from django.db import models
from django.db.utils import IntegrityError

""" Internal Support """
from Control.choice_lists import FUNCTIONAL_DESIGNATIONS
#from Data.validators import _validate_data
from Procedure.validators import _validate_procedure


"""
 Data/models.py
 
 Author(s)   : Matthew J Swann     
 Version     : 1.0
 Last Update : 2013-07-30
 Update by   : Matthew J Swann
 
"""


#TABLE: Data
class Data(models.Model):
    """
     Representation of a singular data item within a PE file.
     
     Primary Keys naturally installed and maintained by Django.
    """
    # identifying marker for procedure in connection with PE information itself
    # Unique being true and defaulting to blank string guards against 'use-less' data
    data_id           = models.CharField(max_length=10, unique=True, blank=True, default='')
    data_tag          = models.CharField(max_length=10, blank=True, default='', null=True)
    calling_functions = models.ManyToManyField('Procedure.Procedure', related_name='data_i_manipulate', null=True, blank=True)
    description       = models.TextField(blank=True, default='', null=True)
    topic             = models.CharField(max_length=1, default='U', choices=FUNCTIONAL_DESIGNATIONS)
    last_modified     = models.DateTimeField(null=True)
    
    class Meta:
        verbose_name        = 'Datum'
        verbose_name_plural = 'Data'
    
    
    def __unicode__(self):
        return '%s : %s -> %s' % ( self.data_id, self.data_tag, self.size )
    
    
    def save(self, *args, **kwargs):
        """
        Time tracks changes via save over-ride.
        """
        self.last_modified = datetime.now()
        super(Data, self).save(*args, **kwargs)

    #SUB_BLOCK: Links to other Procedures
    def add_calling_function(self, procedure):
        """
        Adds a procedure object to the calling_functions table.
        
        @param procedure : Procedure object
        """
        procedure = _validate_procedure( procedure )
        
        self.calling_functions.add( procedure )
        
        
    def remove_calling_function(self, procedure):
        """
        Removes a procedure object to the calling_functions table.
        
        @param procedure : Procedure object
        """
        procedure = _validate_procedure( procedure )
        
        self.calling_functions.remove( procedure )

        

"""
 {
  General Function Block
 }
"""#BLOCK: General Function Block
def create_data(data_id, data_tag=None, topic=None, description=None):
    """
    Creates a procedure object and returns it.
    
    @param data_id     : Sub_routine identification
    @param data_tag    : Short english name for data
    @param topic       : Sub heading
    @param description : Appendations
    
    @raise ValidationError : If parameters are of improper types.
    @return { procedure } : Procedure object --> or NONE if failed creation
    """
    if not ( isinstance(data_id, unicode) or isinstance(data_id, str) ):
        raise ValidationError('create_data() requires string/unicode for routine_id')
    if not ( isinstance(data_tag, unicode) or isinstance(data_tag, str) or (data_tag == None) ):
        raise ValidationError('create_data() requires string/unicode/None for routine_tag')
    if not ( isinstance(topic, unicode) or isinstance(topic, str) or (topic == None) ):
        raise ValidationError('create_data() requires string/unicode/None for topic')
    if not ( isinstance(description, unicode) or isinstance(description, str) or (description == None) ):
        raise ValidationError('create_data() requires string/unicode/None for description')
    
    if ( data_tag == None ):
        data_tag = ''    
    if ( topic == None ):
        topic = 'U'
    if ( description == None ):
        description = ''
    
    try:
        current = Data.objects.create(
                    data_id     = data_id,
                    data_tag    = data_tag,
                    topic       = topic,
                    description = description
                        )
    except IntegrityError:
        current = None
    
    return current
        
        