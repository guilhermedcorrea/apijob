from functools import wraps

def produtos(f):
    @wraps(f)
    def insert_Valores(*args, **kwds):
        print('Calling decorated function')
        return f(*args, **kwds)
    return insert_Valores

@produtos
def update_valores():
    """Docstring"""
    print('Called example function')

update_valores()