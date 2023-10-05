
from . datasets import *



def get_dataset_by_name(name):
	dataset = eval( f'{name}()' )
	return dataset