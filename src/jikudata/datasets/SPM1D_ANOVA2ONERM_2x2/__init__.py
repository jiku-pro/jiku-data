
from ... _cls import _Dataset



class SPM1D_ANOVA2ONERM_2x2(_Dataset):
	
	def _set_attrs(self):
		self.dim        = 1
		self.cite       = None
		self.www        = None
		self.notes      = None

	def _set_expected(self):  # expected_results.npz loaded automatically
		self.expected.tol.z                 = 1e-5
		self.expected.tol.df                = 1e-3
		self.expected.tol.fwhm              = 1e-5
		self.expected.tol.resels            = 1e-5
		self.expected.tol.zc                = 1e-5
		self.expected.tol.p                 = 1e-5
		self.expected.tol.cluster_centroid  = 1e-5
		self.expected.tol.cluster_endpoints = 1e-5
		self.expected.tol.cluster_extent    = 1e-5
		self.expected.tol.cluster_p         = 1e-5

	def _set_params(self):
		from ... _cls import SPM1DParameters
		self.params                  = SPM1DParameters()
		self.params.testname         = 'anova2onerm'
		self.params.args             = self.y, self.x
		self.params.inference_args   = (0.05,)
		self.params.inference_kwargs = dict(method='rft')
