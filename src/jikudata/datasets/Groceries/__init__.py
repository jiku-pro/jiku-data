
import os
import numpy as np
from ... _cls import _Dataset, ExpectedResults, SPM1DParameters



class Groceries(_Dataset):
	
	def _set_attrs(self):
		self.datafile   = os.path.join(  os.path.dirname( __file__ ), 'data.csv'  )
		self.www        = 'https://ww2.coastal.edu/kingw/statistics/R-tutorials/repeated.html'
		
	def _set_expected(self):
		e             = ExpectedResults()
		e.STAT        = 'F'
		e.z           = 4.344
		e.df          = (3, 27)
		e.p           = 0.0127
		e.tol.z       = 0.001
		e.tol.df      = 1e-05
		e.tol.p       = 0.0001
		self.expected = e
		
	def _set_params(self):
		self.params                  = SPM1DParameters()
		self.params.testname         = 'anova1rm'
		self.params.args             = self.y, self.x
		self.params.inference_args   = (0.05,)
		self.params.inference_kwargs = dict(method='param')


