
import os
import numpy as np
from ... _cls import _Dataset, ExpectedResultsListSPM1D, SPM1DParameters



class Syn0D_ANOVA2ONERM_3x4(_Dataset):
	
	def _set_attrs(self):
		self.www        = None
		
	def _set_expected(self):
		z             = (1.013, 0.731, 0.757)
		df            = ((2, 27), (3, 81), (6, 81))
		p             = (0.377, 0.536, 0.606)
		e             = ExpectedResultsListSPM1D('F', z, df, p)
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


