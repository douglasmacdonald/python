'''Convenience functions relying on the sys module.'''

import sys

def path_to_main():
    '''Return the path of the script where function launched. The program root 
    directory.'''

    return sys.path[0]
