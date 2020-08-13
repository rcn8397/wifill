#!/usr/bin/env python3
import os
import sys
import pdb

# Add the pycore library root to the path (Fix this at some point)
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../lib/pycore')))

from core.process import Process

class Cell ( object ):
    '''
    Cell data object
    '''
    def __init__( self, name ):
        self.name       = name
        self.address    = None
        self.essid      = None
        self.protocol   = None
        self.mode       = None
        self.frequency  = None
        self.channel    = None
        self.encryption = None
        self.bitrate    = 0
        self.quality    = 0.0
        self.signal     = 0.0
        try:
            self.index = self.name.split( ' ' )
        except Exception:
            pass

    def debug( self ):
        for x in vars( self ):
            print( '{0} = {1}'.format( x, vars( self )[ x ] ) )
            

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
    def __init__( self, interface = None ):
        super( iwlist, self ).__init__()
        self._cmd       = 'iwlist'
        self.parse_interfaces()
        self.interface  = interface
        self.cells      = dict()
        self.essid2cell = dict()
        
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

    def parse_scan( self ):
        proc = self.irun( 'scanning' )

        # Clear out old data
        self.cells.clear()
        self.essid2cell.clear()
        
        name    = None
        for line in proc.output:
            sys.stdout.write( line )
            if 'Cell' in line:
                tokens             = line.split( ' - ' )
                name               = tokens[0].strip()
                current_cell       = name
                cell               = Cell( name )
                cell.address       = tokens[1][ len( 'address' ) + 1 : ].strip()
                self.cells[ name ] = ( cell )
            elif 'ESSID' in line:
                essid = line.split( ':' )[1].strip().replace('"', '' )
                self.cells[ name ].essid = essid
                self.essid2cell[ essid ] = name
            elif 'Protocol' in line:
                self.cells[ name ].protocol = line.split( ':' )[1].strip()
            elif 'Mode' in line:
                self.cells[ name ].mode = line.split( ':' )[1].strip()
            elif 'Frequency' in line:
                tokens = line.split( ':' )
                self.cells[ name ].frequency = tokens[1][ : tokens[1].index( ' (Channel' ) ]
                # Parse the channel information
                chan_substr           = ' (Channel'
                chan_substr_index     = tokens[1].index( ' (Channel')
                chan_substr_len       = len( chan_substr )
                chan_substr_start     = chan_substr_index + chan_substr_len
                chan_substr_end       = tokens[1].index( ')' )
                self.cells[ name ].channel = tokens[1][ chan_substr_start  : chan_substr_end ]
            elif 'Encription key' in line:
                self.cells[ name ].encryption = line.split( ':' )[1].strip()
            elif 'Bit Rates' in line:
                self.cells[ name ].bitrate = line.split( ':' )[1].strip()
            elif 'Quality=' in line:
                qual_str          = 'Quality='
                qual_substr_index = line.index( qual_str )
                sig_str           = 'Signal level='
                sig_substr_index  = line.index( sig_str )
                quality           = line[ qual_substr_index + len( qual_str ): sig_substr_index ].strip()
                signal            = line[ sig_substr_index + len( sig_str ) : ].strip()
                self.cells[ name ].quality = quality
                self.cells[ name ].signal  = signal
            else:
                # All other lines unsupported at this time.
                pass
            
    def scan( self ):
        self.parse_scan()

    def cell( self, essid ):
        try:
            cell = self.essid2cell[ essid ]
        except KeyError as e:
            return None
        return self.cells[ cell ]

# Main
def main():
    
    print( "hello" )
    
    
# Standard biolerplate to call the main() function to begin the program
if __name__ == '__main__':
    main()

    
    
