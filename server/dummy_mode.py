from functools import wraps

def signature(func, args, kwargs):
    """
    Print the signature of a function call
    """
    arg_types = ",".join(" ({0}) {1}".format(x.__class__.__name__, x) for x in args)
    kwa_types = ",".join("({0}) {1} = {2}".format(v.__class__.__name__, k , v) for k,v in kwargs.iteritems())
    
    return "{0}({1} {2})".format(func.__name__, arg_types if len(arg_types) != 0 else "", 
                                 ", " + kwa_types if len(kwa_types) != 0 else "")
    

def has_dummy_mode(orig_func):
    '''
    Wrapper to give a function a dummy mode: when DUMMY_MODE is True, 
    the wrapped function simply prints its signal, otherwise it behaves as
    defined
    '''
    @wraps(orig_func)
    def wrapped_function(*args, **kwargs):
        if smellie_config.DUMMY_MODE is False:
            return orig_func(*args, **kwargs)
        else:
            print signature(orig_func, args, kwargs)
    return wrapped_function
