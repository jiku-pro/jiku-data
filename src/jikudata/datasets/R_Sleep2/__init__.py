from ... _cls import _Dataset, ExpectedResults, ParametersSPM1D


class R_Sleep2(_Dataset):
    '''
    Student's sleep data, as two independent samples (10 + 10).
    effectsize also reports g = -0.796935239191.
    Checks spm1d's effect_size() against an independent implementation on
    public data -- the same pattern the v0.5 numerics use against the MATLAB
    reimplementations. No inference is run: an effect size is descriptive.
    '''

    def _set_attrs(self):
        self.www   = 'https://easystats.github.io/effectsize/'
        self.notes = 'R built-in dataset "sleep". Expected values computed with R\'s "effectsize" package (1.0.3, R 4.6.1) -- a cross-implementation reference, not a published figure. Generator: effectsize_reference.R.'

    def _set_expected(self):
        e             = ExpectedResults()
        e.STAT        = 'd'
        e.z           = -0.83218108135
        e.tol.z       = 1e-9
        self.expected = e

    def _set_params(self):
        self.params             = ParametersSPM1D()
        self.params.testname    = 'ttest2'
        self.params.args        = self.y, self.x
        self.params.kwargs      = dict( cov_model='iid' )
        self.params.result      = 'effect_size'
        self.params.fwhm_method = None
