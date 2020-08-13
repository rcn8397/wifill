import os
import sys
import pdb

# Add the pycore library root to the path (Fix this at some point)
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../lib/pycore')))

from iwlist_intf import iwlist
from data        import DataStore

class Sampler( object ):
    def __init__( self, name = None, dimension = 1, max_samples = None ):
        if name is None:
            name = self.__class__.__name__
        super( Sampler, self )
        self.name        = name
        self.samples     = DataStore( name, dimension )
        self.stores      = self.samples.store_names()
        self.active      = 0
        self.max_samples = max_samples
        if max_samples is not None:
            self.max_samples_per_store = max_samples / dimension
        else:
            self.max_samples_per_store = None

    def append( self, value ):
        self.samples.append( self.active, value )

    def insert( self, index, value ):
        store = self.stores[ self.active ]
        self.insert2store( strore, index, value )

    def insert2store( self, store, index, value ):
        self.samples[ store ].insert( index, value )

    def next( self ):
        self.active += 1
        self._check_for_roll_over()

    def _check_for_roll_over(self):
        if self.active >= self.samples.num_stores():
            self.active = 0
        
    def set_active( self, index ):
        self.active = index
        self._check_for_roll_over() # not sure we shouldn't just die here

    def num_samples( self, store ):
        return len( self.samples[ store ] )
    
    def num_active_samples( self ):
        return self.num_samples( self.active )
    
    def sample( self, value ):
        if self.max_samples_per_store is not None:
            if len( self.num_active_samples() ) >= self.max_samples_per_store:
                self.next()
        self.append( value )

    def insert_sample( self, index, value ):
        self.insert( index, value )

    def store_sample( self, store, index, value ):
        self.insert2store( store, index, value )
        

class Scanner( Sampler ):
    def __init__( self, interface, name = None, dimension = 4, max_samples = None ):
        if name is None:
            name = interface
        super( Scanner, self ).__init__( name, dimension )
        self.iwlist = iwlist( interface )

    def scan( self ):
        self.iwlist.scan()

class SignalScanner( Scanner ):
    
    def scan( self, essid ):
        super( SignalScanner, self ).scan()
        cell = self.iwlist.cell( essid )
        if cell.signal is not None:
            tokens      = cell.signal.split( '/' )
            numerator   = float(tokens[0])
            denominator = float(tokens[1])
            strength    = numerator/denominator
            self.sample( strength )

        
        

