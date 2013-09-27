""" Python Package Support """
# Not Applicable 

""" Django Package Support """
from django.core.exceptions import ValidationError

""" Internal Package Support """
# Not Applicable

"""
Login_Registration/validators.py

Author:      Matthew J Swann
Version:     1.0
Last Update: 2013-08-12
Update By:   Matthew J Swann

"""


def _validate_profile(profile):
    """
    Helper function which validates the profile parameter in the active knoll handler function,
    and returns the profile if validated.

    @param profile:     Profile object to be validated.
    @raise ValueError:     Raised if the passed in profile is not a profile object.
    @return:             The validated profile object.
    """
    from Login_Registration.models import Profile
    if isinstance(profile, Profile):
        return profile
    else:
        raise TypeError('_validate_profile() must be a valid Profile object.')
    