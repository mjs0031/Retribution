""" Python Support """
import random, string
from datetime import datetime, date

""" Django Support """
from django.core.exceptions import ValidationError
from django.db import models
from django.db.utils import IntegrityError
from django.contrib.localflavor.us import models as us_models
from django.contrib.auth.models import User

""" Internal Support """
from Control.choice_lists import FUNCTIONAL_DESIGNATIONS, SIZE_DESIGNATIONS
from Component.validators import _validate_procedure


"""
 Login_Registration/models.py
 
 Author(s)   : Matthew J Swann     
 Version     : 1.0
 Last Update : 2013-08-12
 Update by   : Matthew J Swann
 
"""

#TABLE: Profile
class Profile(models.Model):
    """
     Representation of a singular user profile.
     
     Primary Keys naturally installed and maintained by Django.
    """
    # Shared Fields
    user             = models.OneToOneField(User, related_name='profile', blank=True)
    avatar           = models.ImageField("Avatar", upload_to='avatars', blank=True, null=True)
    addressLineOne   = models.CharField(max_length=128, blank=True, verbose_name='Address Line 1')
    addressLineTwo   = models.CharField(max_length=128, blank=True, verbose_name='Address Line 2')
    city             = models.CharField(max_length=32, blank=True)
    state            = us_models.USStateField()
    zipCode          = models.CharField(max_length=15, blank=True, verbose_name='Zip Code')
    phone            = us_models.PhoneNumberField(blank=True)
    # Control Fields
    is_registered    = models.BooleanField(default=False)
    activation_key   = models.CharField(max_length=50, blank=True, default='')
    date_initialized = models.DateField(default=date.today())

    def __unicode__(self):
        return '%s %s' % (self.user.first_name, self.user.last_name)


    def set_activation_key(self):
        """
        Sets the activation key for the current profile.
        
        A random key is generated. If it matched any other key in the database, a new key is
        generated.
        """
        field_set = False
        
        while ( field_set == False ) :
            key = ''.join(random.choice(string.digits) for n in range(50))
            
            try:
                Profile.objects.get(activation_key=key)
            
            except Profile.DoesNotExist:
                self.activation_key = key
                self.save()
                field_set = True