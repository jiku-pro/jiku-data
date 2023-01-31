
import os
import numpy as np
from ... _cls import _Dataset, ExpectedResults, SPM1DParameters
# from ... io import load_csv



class Trees(_Dataset):
	
	def _set_attrs(self):
		self.www        = 'https://www.r-bloggers.com/2021/07/how-to-do-a-simple-linear-regression-in-r/'
		self.notes      = 'R dataset:  "data(trees)"; only first two columns ("Girth" and "Height" included in attached data file)'
		
	def _set_expected(self):
		e             = ExpectedResults()
		e.STAT        = 'T'
		e.z           = 3.272
		e.df          = 1, 29
		e.p           = 0.00276
		e.tol.z       = 1e-3
		e.tol.df      = 1e-3
		e.tol.p       = 1e-5
		self.expected = e

	def _set_params(self):
		self.params                  = SPM1DParameters()
		self.params.testname         = 'regress'
		self.params.args             = self.y, self.x
		self.params.inference_args   = (0.05,)
		self.params.inference_kwargs = dict(method='param', dirn=0)


