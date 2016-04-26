'''
This module defines a wrapper for functions, printing the function name, arguments and return value
'''

#from config import DEBUG
DEBUG = True

def print_signature(function, args, kwargs):
    '''
    Prints a string of format 
        function_name(arg1, arg2, kwarg1 = , kwarg = 2)
    '''    
    ags = ", ".join(["{0}".format(x) for x in args])
    kwg = ", ".join(["{0} = {1}".format(*x) for x in kwargs.items()])
        
    signature =  "{0}({1}, {2})".format(function.__name__,
                                        ags,
                                        kwg)
    print signature

def optional_debug(orig_func):
    '''
    A wrapper that forces a print of a formatted signature if DEBUG is set
    to true
    '''
    def wrapped(*args, **kwargs):
        if DEBUG is True:
            print_signature(orig_func, args, kwargs)
        return orig_func(*args, **kwargs)
    return wrapped
