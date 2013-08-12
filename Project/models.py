""" Python Support """
from datetime import datetime, date

""" Django Support """
from django.core.exceptions import ValidationError
from django.db import models
from django.db.utils import IntegrityError

""" Internal Support """
from Control.choice_lists import FUNCTIONAL_DESIGNATIONS, SIZE_DESIGNATIONS
from Component.validators import _validate_procedure


"""
 Project/models.py
 
 Author(s)   : Matthew J Swann     
 Version     : 1.0
 Last Update : 2013-08-12
 Update by   : Matthew J Swann
 
"""

#TABLE: Project
class Project(models.Model):
    """
    Representation of a singular software decompilation project.
    
    Primary Keys naturally installed and maintained by Django.
    """
    project_name        = models.CharField(max_length=64)
    initialization_date = models.DateField(default=date.today())
    last_modified       = models.DateTimeField(null=True, blank=True, verbose_name='Mod Date')


    class Meta:
        verbose_name        = 'Project'
        verbose_name_plural = 'Projects'
    
    
    def __unicode__(self):
        return '%s : %s' % ( self.project_name, self.initialization_date )
    
    
    def save(self, *args, **kwargs):
        """
        Time tracks changes via save over-ride.
        """
        self.last_modified = datetime.now()
        super(Project, self).save(*args, **kwargs)
