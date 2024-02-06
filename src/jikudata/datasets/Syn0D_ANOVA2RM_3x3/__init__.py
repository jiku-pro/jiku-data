
import os
import numpy as np
from ... _cls import _Dataset, ExpectedResultsListSPM1D, SPM1DParameters



class Syn0D_ANOVA2RM_3x3(_Dataset):
	
	def _set_attrs(self):
		self.www        = None
		
	def _set_expected(self):
		z             = (0.173, 0.048, 1.691)
		df            = ((2, 8), (2, 8), (4, 16))
		p             = (0.844, 0.953, 0.201)
		e             = ExpectedResultsListSPM1D('F', z, df, p)
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


