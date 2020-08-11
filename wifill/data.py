#!/usr/bin/env python3
import os
import sys
import pdb
import pandas as pd

# Add the pycore library root to the path (Fix this at some point)
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../lib/pycore')))


class DataStore( object ):
    def __init__( self, name = 'Sample', dimension = 2 ):
        self.data = dict()
        self.data_sets = [ '{0}-{1}'.format( name, i ) for i in range( dimension ) ]
        

    
