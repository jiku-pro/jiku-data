
from .. util import DisplayParams, tuple2simplestr

descriptions = {
	'ttest'             : 'One-sample t-test',
	'ttest2'            : 'Two-sample t-test',
	'ttest_paired'      : 'Paired t-test',
	'regress'           : 'Linear regression',
	
	'anova1'            : 'One-way ANOVA',
	'anova1rm'          : 'One-way repeated measures ANOVA',
	'anova2'            : 'Two-way ANOVA',
	'anova2nested'      : 'Two-way ANOVA (nested)',
	'anova2rm'          : 'Two-way repeated measures ANOVA',
	'anova2onerm'       : 'Two-way ANOVA (repeated measures on one factor)',
	'anova3'            : 'Three-way ANOVA',
	'anova3nested'      : 'Three-way ANOVA (nested)',
	'anova3rm'          : 'Three-way ANOVA (repeated measures on all factors)',
	'anova3onerm'       : 'Three-way ANOVA (repeated measures on one factor)',
	'anova3tworm'       : 'Three-way ANOVA (repeated measures on two factors)',
	
	'cca'               : 'Canonical correlation analysis',
	'hotellings'        : "One-sample Hotelling's T2-test",
	'hotellings2'       : "Two-sample Hotelling's T2-test",
	'hotellings_paired' : "Paired Hotelling's T2-test",
	'manova1'           : 'One-way MANOVA',
	
	'ci_onesample'      : 'One-sample confidence interval',
	'ci_pairedsample'   : 'Paired-sample confidence interval',
	'ci_twosample'      : 'Two-sample confidence interval',
	
	'normality'         : "Normality test",
	'normality_k2'      : "Normality test (D'Agostino-Pearson K2)",
	'normality_sw'      : 'Normality test (Shapiro-Wilk)',

}



class SPM1DParameters(object):
	def __init__(self):
		self.packagename      = 'spm1d'
		self.packageroot      = 'spm1d.stats.c'
		self.testname         = None   # spm1d.stats function name
		self.args             = ()
		self.kwargs           = {}
		self.inference_args   = ()
		self.inference_kwargs = {}
		
	def __repr__(self):
		dp      = DisplayParams( self, default_header=True )
		dp.add( 'testname' )
		dp.add( 'test_description' )
		dp.add( 'args', tuple2simplestr )
		dp.add( 'kwargs' )
		return dp.asstr()

	@property
	def fnname(self):
		return self.packageroot + '.' + self.testname
	@property
	def iargs(self):
		return self.inference_args
	@property
	def ikwargs(self):
		return self.inference_kwargs
	@property
	def isrm(self):
		return self.testname.endswith('rm')
	@property
	def test_description(self):
		return descriptions[ self.testname ]
	
	
	def get_exec_str(self, dataset, aslist=False):
		s = []
		if dataset.dim==1:
			s.append('import matplotlib.pyplot as plt')
		s.append(  'import jikudata as jd')
		s.append( f'import {self.packageroot}' )
		s.append( '' )
		s.append( f'dataset = jd.{dataset.name}()' )
		s.append( '' )
		s.append(  'args    = dataset.params.args')
		s.append(  'kwargs  = dataset.params.kwargs')
		s.append(  'iargs   = dataset.params.iargs')
		s.append(  'ikwargs = dataset.params.ikwargs')
		s.append( f'spmi    = {self.packageroot}.{self.testname}(*args, **kwargs).inference(*iargs, **ikwargs)')
		s.append( '' )
		if dataset.dim==0:
			s.append( 'print( spmi )' )
		elif dataset.dim==1:
			s.append( 'plt.figure()' )
			s.append( 'ax = plt.axes()' )
			s.append( 'spmi.plot( ax=ax )')
			s.append( 'plt.show()')
		if not aslist:
			s = '\n'.join( s )
		return s
		
	
	def get_function(self):
		import spm1d.stats.c
		return eval(  f'spm1d.stats.c.{self.testname}' )
	
	def run(self, kwargs={}, ikwargs={}):
		fn = self.get_function()
		a0 = self.args
		k0 = self.kwargs
		a1 = self.inference_args
		k1 = self.inference_kwargs
		k0.update( kwargs )
		k1.update( ikwargs )
		return fn( *a0 , **k0 ).inference(*a1, **k1)
	
	