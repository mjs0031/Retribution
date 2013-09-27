""" Python Support """
import pytz

""" Django Support """
# Not Applicable

""" Internal Support """
# Not Applicable


"""
 Control/choice_lists.py
 
 Author(s)   : Matthew J swann     
 Version     : 1.0
 Last Update : 2013-09-26
 Update by   : Matthew J Swann
 
"""

FUNCTIONAL_DESIGNATIONS = (
    ('A', '~ Data Processing Algorithm ~'),
    ('I', '~ File/User Input ~'),
    ('M', '~ Main/Start ~'),
    ('N', '~ Network ~'),
    ('S', '~ Internal Support ~'), 
    ('V', '~ Validation ~'),
    ('U', '~ Unknown ~')
        )

SIZE_DESIGNATIONS = (
    ('B', 'byte'),
    ('D', 'd-word'),
    ('Q', 'q-word'),
    ('W', 'word'),
    ('X', 'other/array')             
        )

TZINFOS = (
        ('US/Alaska'),
        ('US/Aleutian'),
        ('US/Arizona'),
        ('US/Central'),
        ('US/East-Indiana'),
        ('US/Eastern'),
        ('US/Hawaii'),
        ('US/Indiana-Starke'),
        ('US/Michigan'),
        ('US/Mountain'),
        ('US/Pacific'),
        ('US/Pacific-New'),
        ('US/Samoa')
    )

