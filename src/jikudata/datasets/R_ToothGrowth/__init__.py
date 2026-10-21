from ... _cls import _Dataset, ExpectedResultsList, ParametersSPM1D


class R_ToothGrowth(_Dataset):
    '''
    Guinea pig odontoblast length by supplement and dose; 2 x 3, balanced.
    Effects in order: supp, dosef, supp:dosef.
    Checks spm1d's effect_size() against an independent implementation on
    public data -- the same pattern the v0.5 numerics use against the MATLAB
    reimplementations. No inference is run: an effect size is descriptive.
    '''

    def _set_attrs(self):
        self.www   = 'https://easystats.github.io/effectsize/'
        self.notes = 'R built-in dataset "ToothGrowth". Expected values computed with R\'s "effectsize" package (1.0.3, R 4.6.1) -- a cross-implementation reference, not a published figure. Generator: effectsize_reference.R.'

    def _set_expected(self):
        e             = ExpectedResultsList( [0.22382544776, 0.773109176761, 0.132027912362], STAT='eta2p' )
        e.tol.z       = 1e-9
        self.expected = e

    def _set_params(self):
        self.params             = ParametersSPM1D()
        self.params.testname    = 'anova2'
        self.params.args        = self.y, self.x
        self.params.kwargs      = dict( cov_model='iid' )
        self.params.result      = 'effect_size'
        self.params.fwhm_method = None
