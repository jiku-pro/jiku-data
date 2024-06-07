
# from . Besier2009muscleforces import Besier2009muscleforces


import os
__all__ = []
for s in sorted( os.listdir( os.path.dirname(__file__) ) ):
    if s[0].isupper():
        exec(  f'from . {s} import {s}' )
        __all__.append( s )
del os, s


_skip = ['SpeedPP2DS']


def iter_all():
    for s in __all__:
        if s not in _skip:
            dataset = eval( f'{s}()' )
            yield dataset


def iter_by_testname(name, dim=None):
    for d in iter_all():
        if d.params.testname == name:
            if dim is None:
                yield( d )
            elif d.dim == dim:
                yield( d )


def get_datasetnames_by_testname(name, dim=None):
    dsnames = []
    for d in iter_by_testname(name, dim):
        dsnames.append( d.name )
    return dsnames