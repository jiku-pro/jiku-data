
# from . Besier2009muscleforces import Besier2009muscleforces


import os
__all__ = []
for s in sorted( os.listdir( os.path.dirname(__file__) ) ):
    if s[0].isupper():
        exec(  f'from . {s} import {s}' )
        __all__.append( s )
del os, s


_skip = ['SpeedPP2DS']


def iter_all( _load_data=True ):
    for s in __all__:
        if s not in _skip:
            dataset = eval( f'{s}( _load_data={_load_data} )' )
            yield dataset



# def iter_by_testname(name, dim=None):
#     for d in iter_all():
#         if d.params.testname == name:
#             if dim is None:
#                 yield( d )
#             elif d.dim == dim:
#                 yield( d )


# def get_datasetnames_by_testname(name, dim=None):
#     dsnames = []
#     for d in iter_by_testname(name, dim):
#         dsnames.append( d.name )
#     return dsnames
    
# def get_datasetnames(testname=None, dim=None):
#     datasets = get_datasets( testname, dim )
#     names    = [d.name for d in datasets]
#     return names

# def get_datasets_old(testname=None, dim=None):
#     datasets = []
#     for d in iter_all():
#         if (testname is None) and (dim is None):
#             datasets.append( d )
#         elif (testname is None) and (dim is not None):
#             if d.dim == dim:
#                 datasets.append( d )
#         elif (testname is not None) and (dim is None):
#             if (d.params is not None) and (d.params.testname == testname):
#                 datasets.append( d )
#         elif (testname is not None) and (dim is not None):
#             if (d.params is not None) and (d.params.testname == testname) and (d.dim==dim):
#                 datasets.append( d )
#     return datasets
    
def get_datasets(testname=None, dim=None, result=None):
    names    = get_dataset_names( testname, dim, result=result )
    return [eval( f'{name}()' )  for name in names]

def get_dataset_names(testname=None, dim=None, result=None):
    """
    Dataset names, optionally filtered by test name and dimensionality.

    "result" selects what the dataset's expectation is ABOUT.  The default,
    None, keeps only datasets whose expectation is a TEST RESULT -- which is
    what every caller meant before any other kind existed, and what callers
    that compare z against a test statistic still mean.  Pass a method name,
    e.g. result="effect_size", for the others, or result="any" for both.

    Without this, a dataset carrying an effect size under testname="ttest2"
    would be handed to a caller expecting a t statistic, and compared as one.
    """
    datasets = []
    for d in iter_all( _load_data=False ):
        r = None if (d.params is None) else getattr(d.params, 'result', None)
        if result == 'any':
            pass
        elif result is None:
            if r is not None:
                continue
        elif r != result:
            continue
        if (testname is None) and (dim is None):
            datasets.append( d.name )
        elif (testname is None) and (dim is not None):
            if d.dim == dim:
                datasets.append( d.name )
        elif (testname is not None) and (dim is None):
            if (d.params is not None) and (d.params.testname == testname):
                datasets.append( d.name )
        elif (testname is not None) and (dim is not None):
            if (d.params is not None) and (d.params.testname == testname) and (d.dim==dim):
                datasets.append( d.name )
    return datasets