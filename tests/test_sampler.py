import os
import sys
import pdb

# Add the project root to the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from wifill import sampler

def test_sampler():
    print( 'Testing Sampler' )
    scanner = sampler.Scanner()

    for i in range( scanner.samples.num_stores() + 1):
        print( 'Loop index: {0}'.format( i ) )
        print( scanner.active )
        scanner.next()
        print( scanner.active )
        

    pdb.set_trace()
    
def main():
    test_sampler()

if __name__ == '__main__':
    main()
