""" Python Support """
from datetime import datetime

""" Django Support """
from django.core.exceptions import ValidationError
from django.db import models
from django.db.utils import IntegrityError

""" Internal Support """
from Control.choice_lists import FUNCTIONAL_DESIGNATIONS, SIZE_DESIGNATIONS
from Component.validators import _validate_procedure


"""
 Component/models.py
 
 Author(s)   : Matthew J Swann     
 Version     : 1.0
 Last Update : 2013-08-31
 Update by   : Matthew J Swann
 
"""


#TABLE: Data
class Data(models.Model):
    """
     Representation of a singular data item within a PE file.
     
     Primary Keys naturally installed and maintained by Django.
    """
    # Keyed Fields
    calling_functions = models.ManyToManyField('Component.Procedure', related_name='data_i_manipulate', 
                                               blank=True, verbose_name='Calling Functions')
    # Natural Fields
    data_id           = models.CharField(max_length=16, unique=True, verbose_name='Data ID')
    data_tag          = models.CharField(max_length=32, blank=True,  verbose_name='Data Tag')
    description       = models.CharField(max_length=256, blank=True)    
    topic             = models.CharField(max_length=1, default='U', choices=FUNCTIONAL_DESIGNATIONS)
    size              = models.CharField(max_length=1, default='', choices=SIZE_DESIGNATIONS)
    last_modified     = models.DateTimeField(null=True, blank=True, verbose_name='Mod Date')
    
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


#TABLE: Export
class Export(models.Model):
    """
     Representation of a singular export item within a PE file.
     
     Primary Keys naturally installed and maintained by Django.
    """
    export_id     = models.CharField(max_length=16, unique=True, verbose_name='Export ID')
    export_tag    = models.CharField(max_length=32, blank=True,  verbose_name='Export Tag')
    description   = models.CharField(max_length=256, blank=True)
    last_modified = models.DateTimeField(null=True, blank=True, verbose_name='Mod Date')
    
    class Meta:
        verbose_name        = 'Export'
        verbose_name_plural = 'Exports'
    
    
    def __unicode__(self):
        return '%s : %s --> %s' % ( self.export_id, self.export_tag, self.description )
    
    
    def save(self, *args, **kwargs):
        """
        Time tracks changes via save over-ride.
        """
        self.last_modified = datetime.now()
        super(Export, self).save(*args, **kwargs)
    

#TABLE: Import
class Import(models.Model):
    """
     Representation of a singular import item within a PE file.
     
     Primary Keys naturally installed and maintained by Django.
    """
    import_id     = models.CharField(max_length=16, unique=True,verbose_name='Import ID')
    import_tag    = models.CharField(max_length=32, blank=True, verbose_name='Import Tag')
    library       = models.CharField(max_length=32, blank=True)
    description   = models.CharField(max_length=256, blank=True)
    last_modified = models.DateTimeField(null=True, blank=True, verbose_name='Mod Date')
    
    class Meta:
        verbose_name        = 'Import'
        verbose_name_plural = 'Imports'
    
    
    def __unicode__(self):
        return '%s : %s --> %s' % ( self.import_id, self.import_tag, self.library )
    
    
    def save(self, *args, **kwargs):
        """
        Time tracks changes via save over-ride.
        """
        self.last_modified = datetime.now()
        super(Import, self).save(*args, **kwargs)


#TABLE: Metadata
class Metadata(models.Model):
    """
     Representation of any metadata associated with a compnent object
     
     Primary Keys naturally installed and maintained by Django.
    """
    # Keyed Fields
    component = models.CharField(max_length=16, verbose_name='Component Tag')
    # Natural Fields
    encrypted                  = models.NullBooleanField(default=None, null=True, verbose_name='Encrypted')
    self_modifying             = models.NullBooleanField(default=None, null=True, verbose_name='Self Modifying')
    self_mod_contained_to_self = models.NullBooleanField(default=None, null=True, verbose_name='Self Modifying - Contained')
    encryption_type            = models.CharField(max_length=32, default='None' , verbose_name='Encryption Type')
    last_modified              = models.DateTimeField(null=True, blank=True, verbose_name='Mod Date')
    
    class Meta:
        verbose_name        = 'Metadata'
        verbose_name_plural = 'Metadata'
    
    
    def __unicode__(self):
        return 'meta --> %s' % ( self.get_component() )
    
    
    def save(self, *args, **kwargs):
        """
        Time tracks changes via save over-ride.
        """
        self.last_modified = datetime.now()
        super(Metadata, self).save(*args, **kwargs)


    def get_component(self):
        """
        """
        return 'LOL --> Finish me!'

#TABLE: Procedure
class Procedure(models.Model):
    """
     Representation of a singular sub-routine within a PE file.
     
     Primary Keys naturally installed and maintained by Django.
    """
    # identifying marker for procedure in connection with PE information itself
    # Unique being true and defaulting to blank string guards against 'use-less' data
    routine_id        = models.CharField(max_length=16, unique=True, verbose_name='Routine ID')
    routine_tag       = models.CharField(max_length=32, blank=True,  verbose_name='Routine Tag')
    calling_functions = models.ManyToManyField('self', related_name='functions_i_call', 
                                               blank=True, verbose_name='Calling Functions')
    called_functions  = models.ManyToManyField('self', related_name='functions_calling_me', 
                                               blank=True, verbose_name='Called Functions')
    description       = models.CharField(max_length=256, blank=True)
    topic             = models.CharField(max_length=1, default='U', choices=FUNCTIONAL_DESIGNATIONS)
    last_modified     = models.DateTimeField(null=True, blank=True, verbose_name='Mod Date')    
    
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
def create_data(data_id, data_tag=None, size=None, topic=None, description=None):
    """
    Creates a data object and returns it.
    
    @param data_id     : Data identification
    @param data_tag    : Short english name for data
    @param size        : Size of the data item
    @param topic       : Sub heading
    @param description : Appendations
    
    @raise ValidationError : If parameters are of improper types.
    @return { data }       : Data object --> or NONE if failed creation
    """
    if not ( isinstance(data_id, unicode) or isinstance(data_id, str) ):
        raise ValidationError('create_data() requires string/unicode for data_id')
    if not ( isinstance(data_tag, unicode) or isinstance(data_tag, str) or (data_tag == None) ):
        raise ValidationError('create_data() requires string/unicode/None for data_tag')
    if not ( isinstance(size, unicode) or isinstance(size, str) or (size == None) ):
        raise ValidationError('create_data() requires string/unicode/None for size')
    if not ( isinstance(topic, unicode) or isinstance(topic, str) or (topic == None) ):
        raise ValidationError('create_data() requires string/unicode/None for topic')
    if not ( isinstance(description, unicode) or isinstance(description, str) or (description == None) ):
        raise ValidationError('create_data() requires string/unicode/None for description')
    
    if ( data_tag == None ):
        data_tag    = ''
            
    if ( size == None ):
        size        = ''
    
    if ( topic == None ):
        topic       = 'U'
        
    if ( description == None ):
        description = ''
    
    try:
        current = Data.objects.create(
                    data_id     = data_id,
                    data_tag    = data_tag,
                    size        = size,
                    topic       = topic,
                    description = description
                        )
    except IntegrityError:
        current = None
    
    return current
        

def create_export():
    """
    Creates an export objects and returns it
    
    @param :
    @param :
    @param :
    @param :  
    
    @raise ValidationError : If parameters are of improper types.
    @return { export }     : Export object --> or NONE if failed creation

    """
    pass


def create_import():
    """
    Creates an import objects and returns it
    
    @param :
    @param :
    @param :
    @param :  
    
    @raise ValidationError : If parameters are of improper types.
    @return { import }     : Import object --> or NONE if failed creation
    """
    pass


def create_metadata():
    """
    Creates a metadata object and returns it
    
    @param :
    @param :
    @param :
    @param :  
    
    @raise ValidationError : If parameters are of improper types.
    @return { metadata }   : Metadata object --> or NONE if failed creation
    """
    pass


def create_procedure(routine_id, routine_tag=None, topic=None, description=None):
    """
    Creates a procedure object and returns it.
    
    @param routine_id  : Sub_routine identification
    @param routine_tag : Short english name for procedure
    @param topic       : Sub heading
    @param description : Appendations
    
    @raise ValidationError : If parameters are of improper types.
    @return { procedure }  : Procedure object --> or NONE if failed creation
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
        topic       = 'U'
        
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
        
        