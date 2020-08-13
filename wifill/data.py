#!/usr/bin/env python3
import os
import sys
import pdb
import pandas as pd

# Add the pycore library root to the path (Fix this at some point)
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../lib/pycore')))


class DataStore( object ):
    def __init__( self, name = 'Sample', dimension = 2 ):
        self.name   = name
        self.data   = dict()
        self.stores = [ '{0}-{1}'.format( name, i ) for i in range( dimension ) ]
        for s in self.stores:
            self.data[ s ] = []
        
    def append( self, store, value ):
        name = self.stores[ store ]
        self.data[ name ].append( value )

    def clear( self ):
        for store in self.data:
            store.clear()

    def remove( self, store, index ):
        store = self.data[ self.store_name( store ) ]
        store.pop( index )

    def num_stores( self ):
        return len( self.stores )
    
    def store_length( self, store ):
        return len( self.data[ self.store_name( store ) ] )        

    def store_name( self, store ):
        return self.stores[ store ]

    def store_names( self ):
        return self.stores

    def add_store( self, name, store = [] ):
        self.data[ name ] = store
        self.stores.append( name )
        return self.stores.index( name )

    def remove_store( self, store ):
        self.data.pop( self.store_name( store ), None )
        self.stores.pop( store )
        

    def to_df( self ):
        return pd.DataFrame( self.data )

    def to_csv( self, fname = None ):
        if fname is None:
            fname = '{0}.csv'.format( self.name )
        self.to_df().to_csv( fname )
