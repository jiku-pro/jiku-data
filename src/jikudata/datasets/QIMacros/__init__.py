
import os
import numpy as np
from ... _cls import _Dataset, ExpectedResultsList, SPM1DParameters



class QIMacros(_Dataset):
	
	def _set_attrs(self):
		self.datafile   = os.path.join(  os.path.dirname( __file__ ), 'data.csv'  )
		self.www        = 'https://www.qimacros.com/hypothesis-testing/anova-two-way-nested-excel/'
		
	def _set_expected(self):
		z             = (0.111, 45.726)
		df            = ((1, 6), (6, 24))
		p             = (0.750, 0.0)
		e             = ExpectedResultsList('F', z, df, p)
		e.tol.z       = 0.001
		e.tol.df      = 1e-05
		e.tol.p       = 0.001
		self.expected = e	

	def _set_params(self):
		self.params                  = SPM1DParameters()
		self.params.testname         = 'anova2nested'
		self.params.args             = self.y, self.x
		self.params.inference_args   = (0.05,)
		self.params.inference_kwargs = dict(method='param')


