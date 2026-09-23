from ... _cls import _Dataset, ExpectedResults, ParametersSPM1D


class R_SleepPaired(_Dataset):
    '''
    Student's sleep data in its PAIRED form.

    Included deliberately: this is where d_z -- standardised by the SD of
    the differences -- and d_av, by the SD of the raw scores, differ most.
    spm1d returns d_z, because ttest_paired fits on the differences, and
    the expectation records d_z.

    Checks spm1d's effect_size() against an independent implementation on
    public data -- the same pattern the v0.5 numerics use against the MATLAB
    reimplementations. No inference is run: an effect size is descriptive.
    '''

    def _set_attrs(self):
        self.www   = 'https://easystats.github.io/effectsize/'
        self.notes = 'R built-in dataset "sleep". Expected values computed with R\'s "effectsize" package (1.0.3, R 4.6.1) -- a cross-implementation reference, not a published figure. Generator: effectsize_reference.R.'

    def _set_expected(self):
        e             = ExpectedResults()
        e.STAT        = 'd_z'
        e.z           = -1.28455756259
        e.tol.z       = 1e-9
        self.expected = e

    def _set_params(self):
        self.params             = ParametersSPM1D()
        self.params.testname    = 'ttest_paired'
        self.params.args        = self.y, self.x
        self.params.result      = 'effect_size'
        self.params.fwhm_method = None
