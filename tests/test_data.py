import os
import sys
import pdb

# Add the project root to the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from wifill import data

def test_data():
    print( 'Testing DataStore' )
    ds = data.DataStore()
    for i in range( 10 ):
        ds.append( 0, float( i ) )
        ds.append( 1, float( 10 - i ) )

    print( ds.data )

    num_stores = ds.num_stores()
    for i in range( num_stores ):
        length = ds.store_length( i )
        name   = ds.store_name( i )
        print( 'Store {0}@{1} has a length of {2}'.format( i, name, length ) )
   
    new_store = [ float( i+20 ) for i in range( 10 ) ]
    index = ds.add_store( 'new_store', new_store )
    print( ds.data )
    print( 'Store {0}@{1} has a length of {2}'.format( index,
                                                       ds.store_name( index ),
                                                       ds.store_length( index ) ) )

    ds.remove_store( index )
    print( ds.data )
    assert num_stores == 2

    ds.to_csv()

    
def main():
    test_data()

if __name__ == '__main__':
    main()
