
import os
import numpy as np
from ... _cls import _Dataset, ExpectedResultsList, SPM1DParameters



class Syn0D_ANOVA2RM_3x5(_Dataset):
	
	def _set_attrs(self):
		self.www        = None
		
	def _set_expected(self):
		z             = (1.632, 0.651, 0.816)
		df            = ((2, 12), (4, 24), (8, 48))
		p             = (0.236, 0.632, 0.592)
		e             = ExpectedResultsList('F', z, df, p)
		e.tol.z       = 0.001
		e.tol.df      = 1e-05
		e.tol.p       = 0.001
		self.expected = e	

	def _set_params(self):
		self.params                  = SPM1DParameters()
		self.params.testname         = 'anova2rm'
		self.params.args             = self.y, self.x
		self.params.inference_args   = (0.05,)
		self.params.inference_kwargs = dict(method='param')


