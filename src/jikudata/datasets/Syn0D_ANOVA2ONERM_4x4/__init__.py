
import os
import numpy as np
from ... _cls import _Dataset, ExpectedResultsList, SPM1DParameters



class Syn0D_ANOVA2ONERM_4x4(_Dataset):
	
	def _set_attrs(self):
		self.www        = None
		
	def _set_expected(self):
		z             = (1.139, 0.193, 0.773)
		df            = ((3, 76), (3, 228), (9, 228))
		p             = (0.339, 0.901, 0.641)
		e             = ExpectedResultsList('F', z, df, p)
		e.tol.z       = 0.001
		e.tol.df      = 1e-05
		e.tol.p       = 0.001
		self.expected = e	

	def _set_params(self):
		self.params                  = SPM1DParameters()
		self.params.testname         = 'anova2onerm'
		self.params.args             = self.y, self.x
		self.params.inference_args   = (0.05,)
		self.params.inference_kwargs = dict(method='param')


