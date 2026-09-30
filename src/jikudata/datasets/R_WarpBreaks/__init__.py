from ... _cls import _Dataset, ExpectedResultsList, ParametersSPM1D


class R_WarpBreaks(_Dataset):
    '''
    Warp breaks by wool type and tension; 2 x 3, balanced.
    Effects in order: wool, tension, wool:tension.
    Checks spm1d's effect_size() against an independent implementation on
    public data -- the same pattern the v0.5 numerics use against the MATLAB
    reimplementations. No inference is run: an effect size is descriptive.
    '''

    def _set_attrs(self):
        self.www   = 'https://easystats.github.io/effectsize/'
        self.notes = 'R built-in dataset "warpbreaks". Expected values computed with R\'s "effectsize" package (1.0.3, R 4.6.1) -- a cross-implementation reference, not a published figure. Generator: effectsize_reference.R.'

    def _set_expected(self):
        e             = ExpectedResultsList( [0.072737706682, 0.261494075023, 0.148606148425], STAT='eta2p' )
        e.tol.z       = 1e-9
        self.expected = e

    def _set_params(self):
        self.params             = ParametersSPM1D()
        self.params.testname    = 'anova2'
        self.params.args        = self.y, self.x
        self.params.kwargs      = dict( cov_model='iid' )
        self.params.result      = 'effect_size'
        self.params.fwhm_method = None
