import os
import sys
import pdb

# Add the pycore library root to the path (Fix this at some point)
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../lib/pycore')))

from iwlist_intf import iwlist
from data        import DataStore

class Sampler( object ):
    def __init__( self, name = None, dimension = 1 ):
        if name is None:
            name = self.__class__.__name__
        super( Sampler, self )
        self.name    = name
        self.samples = DataStore( name, dimension )
        self.active  = 0

    def append( self, value ):
        self.samples[ self.active ].append( value )

    def next( self ):
        self.active += 1
        self._check_active_for_roll_over()

    def _check_active_for_roll_over(self):
        if self.active >= self.samples.num_stores():
            self.active = 0
        
    def set_active( self, index ):
        self.active = index
        self._check_active_for_roll_over() # not sure we shouldn't just die here

class Scanner( Sampler ):
    def __init__( self, name = None, dimension = 4 ):
        if name is None:
            name = self.__class__.__name__
        super( Scanner, self ).__init__( name, dimension )
        

