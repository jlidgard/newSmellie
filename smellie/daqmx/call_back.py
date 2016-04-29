import weakref

""" 
Helper functions to pass data to callback functions

See examples.
"""

# NIDAQmx allows the passing of a pointer to a data structure in a callback function.
# If this function is implemented in Python, we would like this data to be a Python object.
# This object will not (and will not) be used in C but we want to pass a reference to it.
# A workaround is to use the weakref module.
# 
# Define a weakref dictionary to be able to remember objects and retrieve them by ID.
_id2obj_dict = weakref.WeakValueDictionary()

def create_callbackdata_id(obj):
    """ 
    Uses the weakref module to create and store a reference to obj
    
    output value: reference to the object
    
    It is not possible to directly uses a Python object through a callback function, because with ctypes there is no pointer to the Python object.
    This function stores a reference to an object in a dictionary.
    This object can be retrieved using the get_callbackdata_from_id function.
    
    For Python objects that cannot be weakref-erenced, one can create a dummy class to wrap the Python object: 
        def MyList(list)
            pass
            
        data = MyList()
        id = create_callbackdata_id(data)
    """
    oid = id(obj)
    _id2obj_dict[oid] = obj
    return oid

def get_callbackdata_from_id(oid):
    """
    Retrieve an object stored using create_callbackdata_id    
    """
    return _id2obj_dict[oid]
