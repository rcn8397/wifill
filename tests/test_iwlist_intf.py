import os
import sys
import pdb

# Add the project root to the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from wifill import iwlist_intf

def test_iwlist_intf():
    print( 'Testing iwlist interface' )
    w = iwlist_intf.iwlist('wlx98482720364f')
    w.scan()

    
def main():
    test_iwlist_intf()

if __name__ == '__main__':
    main()
