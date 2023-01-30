
import os
import numpy as np
from ... _cls import _Dataset, ExpectedResultsList, SPM1DParameters



class SouthamptonNested1(_Dataset):
	
	def _set_attrs(self):
		self.datafile   = os.path.join(  os.path.dirname( __file__ ), 'data.csv'  )
		self.www        = 'https://www.southampton.ac.uk/~cpd/anovas/datasets/Doncaster&Davey%20-%20Model%202_1%20Two%20factor%20nested.txt'
		
	def _set_expected(self):
		z             = (4.02, 9.26)
		df            = ((2, 3), (3, 18))
		p             = (0.142, 0.001)
		e             = ExpectedResultsList('F', z, df, p)
		e.tol.z       = 0.01
		e.tol.df      = 1e-05
		e.tol.p       = 0.001
		self.expected = e	

	def _set_params(self):
		self.params                  = SPM1DParameters()
		self.params.testname         = 'anova2nested'
		self.params.args             = self.y, self.x
		self.params.inference_args   = (0.05,)
		self.params.inference_kwargs = dict(method='param')


