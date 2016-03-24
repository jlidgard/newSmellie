'''
Processes exceptions thrown by the software, converting them to 
error strings to be sent over the server
'''

HANDLED_EXCEPTIONS = []

def process_exception(exception):
    '''
    Searches through the list of SNODROP exception types, produces a string
    of the format "SNODROP ERROR: <string representation of exception>"
    If the type is not recognised it is sent as Unhandled Exception!
    '''

    thrown_type = exception.__class__
    if thrown_type in HANDLED_EXCEPTIONS:
        return "SNODROP ERROR: {0}".format(repr(exception))
    return "SNODROP ERROR: Unhandled exception!! {0}".format(repr(exception))



def str_wrap_exceptions(orig_function):
    '''
    A wrapper on a function that converts any thrown exceptions into an 
    error string and returns that
    '''

    def modified_function(*args, **kwargs):
        try:
            return orig_function(*args, **kwargs)
        except Exception as e:
            return process_exception(e)

    modified_function.__name__ = orig_function.__name__
    return modified_function    

def test():
    pass

test2 = str_wrap_exceptions(test)
print test.__name__, test2.__name__
