""" Python Support """
from pytz import timezone
from datetime import datetime

""" Django Support """
# Not Applicable

""" Internal Support """
from Control.choice_lists import TZINFOS


"""
 Control/tz_sandbox.py
 
 Author(s)   : Matthew J swann     
 Version     : 1.0
 Last Update : 2013-09-29
 Update by   : Matthew J Swann
 
"""

def main():
    
    now = datetime.now()
    
    fmt = '%Y-%m-%d %H:%M:%S %Z%z'
    
    server = timezone('America/Chicago')
    
    for i in TZINFOS:
        
        current = timezone(i)
        print type(current)
        
        source = current.localize(now)
        print type(source)
        
        normal = source.astimezone(server)
        print type(normal)
        
        print current.zone
        print 'now time in THIS timezone :: %s' % (source.strftime(fmt))
        print ''
        print 'normalized to SERVER time :: %s' % (normal.strftime(fmt))
        print ''
        print ' * * * '
        
        for j in TZINFOS:
            current_two = timezone(j)
            
            forge = current.normalize(normal)
            
            spread = forge.astimezone(current_two) 
            
            print '     --> %s' % (current_two.zone)
            print '     --> SERVER time changed to zone: %s' % (spread.strftime(fmt))
            print ''
        
        print '--- --- --- ---'
        