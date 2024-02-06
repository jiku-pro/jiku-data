
import os
import numpy as np
from ... _cls import _Dataset, ExpectedResultsListSPM1D, SPM1DParameters



class Syn0D_ANOVA2_3x3(_Dataset):
	
	def _set_attrs(self):
		self.www        = None
		
	def _set_expected(self):
		z             = (0.249, 0.036, 1.628)
		df            = ((2, 36), (2, 36), (4, 36))
		p             = (0.781, 0.965, 0.188)
		e             = ExpectedResultsListSPM1D('F', z, df, p)
		e.tol.z       = 0.001
		e.tol.df      = 1e-05
		e.tol.p       = 0.001
		self.expected = e	

	def _set_params(self):
		self.params                  = SPM1DParameters()
		self.params.testname         = 'anova2'
		self.params.args             = self.y, self.x
		self.params.inference_args   = (0.05,)
		self.params.inference_kwargs = dict(method='param')


