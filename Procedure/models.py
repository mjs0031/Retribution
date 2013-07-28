""" Python Support """
from datetime import datetime

""" Django Support """
from django.core.exceptions import ValidationError
from django.db import models
from django.db.utils import IntegrityError

""" Internal Support """
from Control.choice_lists import FUNCTION_DESIGNATIONS
from Procedure.validators import _validate_procedure


"""
 Procedures/models.py
 
 Author(s)   :      
 Version     : 1.0
 Last Update : 2013-07-27
 Update by   : Matthew J Swann
 
"""


#BLOCK: Procedure
class Procedure(models.Model):
    """
     Representation of a singular sub-routine within a PE file.
     
     Primary Keys naturally installed and maintained by Django.
    """
    # identifying marker for procedure in connection with PE information itself
    # Unique being true and defaulting to blank string guards against 'use-less' data
    routine_id        = models.CharField(max_length=10, unique=True, blank=True, default='')
    routine_tag       = models.CharField(max_length=10, blank=True, default='', null=True)
    calling_functions = models.ManyToManyField('self', related_name='functions_i_call', null=True, blank=True)
    called_functions  = models.ManyToManyField('self', related_name='functions_calling_me', null=True, blank=True)
    description       = models.TextField(blank=True, default='', null=True)
    topic             = models.CharField(max_length=1, default='U', choices=FUNCTION_DESIGNATIONS)
    last_modified     = models.DateTimeField(null=True)
    
    class Meta:
        verbose_name        = 'Procedure'
        verbose_name_plural = 'Procedures'
    
    
    def __unicode__(self):
        return '%s : %s -> %s' % ( self.routine_id, self.routine_tag, self.topic )
    
    
    def save(self, *args, **kwargs):
        """
        Time tracks changes via save over-ride.
        """
        self.last_modified = datetime.now()
        super(Procedure, self).save(*args, **kwargs)


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
        
        
    def add_called_function(self, procedure):
        """
        Adds a procedure object to the called_function table.
        
        @param procedure : Procedure object
        """
        procedure = _validate_procedure( procedure )
        
        self.called_function.add( procedure )
        
        
    def remove_called_function(self, procedure):
        """
        Removes a procedure object to the called_function table.
        
        @param procedure : Procedure object
        """
        procedure = _validate_procedure( procedure )
        
        self.called_function.remove( procedure )
        

"""
 {
  General Function Block
 }
"""#BLOCK: General Function Block
def create_procedure(routine_id, routine_tag=None, topic=None, description=None):
    """
    Creates a procedure object and returns it.
    
    @param routine_id  : Sub_routine identification
    @param topic       : Sub heading
    @param description : Appendations
    
    @raise ValidationError : If parameters are of improper types.
    @return { procedure } : Procedure object --> or NONE if failed creation
    """
    if not ( isinstance(routine_id, unicode) or isinstance(routine_id, str) ):
        raise ValidationError('create_procedure() requires string/unicode for routine_id')
    if not ( isinstance(routine_tag, unicode) or isinstance(routine_tag, str) or (routine_tag == None) ):
        raise ValidationError('create_procedure() requires string/unicode/None for routine_tag')
    if not ( isinstance(topic, unicode) or isinstance(topic, str) or (topic == None) ):
        raise ValidationError('create_procedure() requires string/unicode/None for topic')
    if not ( isinstance(description, unicode) or isinstance(description, str) or (description == None) ):
        raise ValidationError('create_procedure() requires string/unicode/None for description')
    
    if ( routine_tag == None ):
        routine_tag = ''    
    if ( topic == None ):
        topic = 'U'
    if ( description == None ):
        description = ''
    
    try:
        current = Procedure.objects.create(
                    routine_id  = routine_id,
                    routine_tag = routine_tag,
                    topic       = topic,
                    description = description
                        )
    except IntegrityError:
        current = None
    
    return current
        
        