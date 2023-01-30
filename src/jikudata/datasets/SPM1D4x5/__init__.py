
import os
import numpy as np
from ... _cls import _Dataset, ExpectedResultsList, SPM1DParameters



class SPM1D4x5(_Dataset):
	
	def _set_attrs(self):
		self.datafile   = os.path.join(  os.path.dirname( __file__ ), 'data.csv'  )
		self.www        = 'None'
		
	def _set_expected(self):
		z             = (1.447, 1.609, 0.868)
		df            = ((3, 36), (4, 144), (12, 144))
		p             = (0.245, 0.175, 0.581)
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


