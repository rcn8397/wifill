#!/usr/bin/env python3
import os
import sys
import pdb

# Add the pycore library root to the path (Fix this at some point)
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../lib/pycore')))

from core.process import Process

class iwlist ( object ):
    '''
    iwlist    Wireless-Tools version 30
              Compatible with Wireless Extension v11 to v22.

    Usage: iwlist [interface] scanning [essid NNN] [last]
                  [interface] frequency 
                  [interface] channel 
                  [interface] bitrate 
                  [interface] rate 
                  [interface] encryption 
                  [interface] keys 
                  [interface] power 
                  [interface] txpower 
                  [interface] retry 
                  [interface] ap 
                  [interface] accesspoints 
                  [interface] peers 
                  [interface] event 
                  [interface] auth 
                  [interface] wpakeys 
                  [interface] genie 
                  [interface] modulation 

    '''

    abbrevcmds = { 'scan'         : 'scanning',
                   'freq'         : 'frequency',
                   'chan'         : 'channel',
                   'bitrate'      : 'bitrate',
                   'rate'         : 'rate',
                   'encryp'       : 'encryp',
                   'keys'         : 'keys',
                   'pow'          : 'power',
                   'txp'          : 'txpower',
                   'retry'        : 'retry',
                   'ap'           : 'ap',
                   'accesspoints' : 'accesspoint',
                   'peers'        : 'peers',
                   'event'        : 'event',
                   'auth'         : 'auth',
                   'wpakeys'      : 'wpakeys',
                   'genie'        : 'genie',
                   'mod'          : 'modulation',
                   
                   'help'         : '--help',
                   'version'      : '-v',
    }
                    
    def __init__( self, interface = None ):
        super( iwlist, self ).__init__()
        self._cmd = 'iwlist'
        self.parse_interfaces()
        self.interface = interface
        if self.interface is None:
            self.print_interfaces()
            sys.exit( 'An interface is required to continue' )
        elif self.interface not in self.interfaces:
            self.print_interfaces()
            sys.exit( 'Unknown interface specified' )
                
    def irun( self, sub ):
        return self.run( sub, interface = self.interface )
    
    def run( self, sub, interface = None ):
        if interface is None:
            interface = ''
        proc = Process( cmd = '{0} {1} {2}'.format( self._cmd, interface, sub ) )
        return proc

    def parse_interfaces( self ):
        proc = self.run( 'ap' )
        self.interfaces = []

        for line in proc.output:
            if '\n' == line:
                continue
            intf = line.split( ' ' )
            self.interfaces.append( intf[ 0 ] )

    def print_interfaces( self ):
        self.parse_interfaces()
        print( 'Discovered Interfaces:' )
        for intf in self.interfaces:
            print( '\t{0}'.format( intf ) )

# Main
def main():
    
    print( "hello" )
    
    
# Standard biolerplate to call the main() function to begin the program
if __name__ == '__main__':
    main()

    
    
