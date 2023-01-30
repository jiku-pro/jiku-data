
import os
import numpy as np
from ... _cls import _Dataset, ExpectedResultsList, SPM1DParameters



class Santa23(_Dataset):
	
	def _set_attrs(self):
		self.datafile   = os.path.join(  os.path.dirname( __file__ ), 'data.csv'  )
		self.www        = 'https://www.statisticshell.com/docs/mixed.pdf'
		
	def _set_expected(self):
		z             = (0.511, 36.946, 3.856)
		df            = ((1, 10), (2, 20), (2, 20))
		p             = (0.491, 0.0, 0.038)
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


