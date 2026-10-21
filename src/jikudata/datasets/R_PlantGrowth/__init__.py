from ... _cls import _Dataset, ExpectedResults, ParametersSPM1D


class R_PlantGrowth(_Dataset):
    '''
    Plant growth under a control and two treatments; balanced, 3 x 10.
    effectsize also reports eta2 = 0.264148296832, omega2 = 0.20407884599.
    Checks spm1d's effect_size() against an independent implementation on
    public data -- the same pattern the v0.5 numerics use against the MATLAB
    reimplementations. No inference is run: an effect size is descriptive.
    '''

    def _set_attrs(self):
        self.www   = 'https://easystats.github.io/effectsize/'
        self.notes = 'R built-in dataset "PlantGrowth". Expected values computed with R\'s "effectsize" package (1.0.3, R 4.6.1) -- a cross-implementation reference, not a published figure. Generator: effectsize_reference.R.'

    def _set_expected(self):
        e             = ExpectedResults()
        e.STAT        = 'eta2p'
        e.z           = 0.264148296832
        e.tol.z       = 1e-9
        self.expected = e

    def _set_params(self):
        self.params             = ParametersSPM1D()
        self.params.testname    = 'anova1'
        self.params.args        = self.y, self.x
        self.params.kwargs      = dict( cov_model='iid' )
        self.params.result      = 'effect_size'
        self.params.fwhm_method = None
