
# from . Besier2009muscleforces import Besier2009muscleforces


import os
__all__ = []
for s in sorted( os.listdir( os.path.dirname(__file__) ) ):
	if s[0].isupper():
		exec(  f'from . {s} import {s}' )
		__all__.append( s )
del os, s



def iter_all():
	for s in __all__:
		dataset = eval( f'{s}()' )
		yield dataset
		
		
def iter_by_testname(name):
	for d in iter_all():
		if d.params.testname == name:
			yield( d )
			
			
def get_datasetnames_by_testname(name):
	dsnames = []
	for d in iter_by_testname(name):
		dsnames.append( d.name )
	return dsnames