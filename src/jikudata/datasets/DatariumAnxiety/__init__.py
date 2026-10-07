
from ... _cls import _Dataset, ExpectedResultsSPM1D, ParametersSPM1D


_notes = '''
Data: datarium::anxiety (45 participants in three exercise groups, anxiety
scored at three time points), as prepared for the one-way ANCOVA tutorial at
https://www.datanovia.com/en/lessons/ancova-in-r/ :  the first time point is
the covariate ("pretest", t1) and the third is the response ("posttest", t3),
and the tutorial sets the posttest of participant 14 to 19 before analysing
(the value in the package is 17.3).  This dataset carries the tutorial's
version, so that its printed table is the expectation.

Results: rstatix::anova_test(posttest ~ pretest + group), which reports the
group effect adjusted for the covariate as F(2, 41) = 218.629, p = 1.35e-22
(the covariate itself:  F(1, 41) = 598.321).  The analysis pools the residual
variance across groups, hence cov_model="iid".

The data sets in datarium are dedicated to the public domain (CC0 1.0).
'''


class DatariumAnxiety(_Dataset):

    def _set_attrs(self):
        self.cite       = 'Kassambara, A. (2019) datarium: Data Bank for Statistical Analysis and Visualization. R package.'
        self.www        = 'https://cran.r-project.org/package=datarium', 'https://www.datanovia.com/en/lessons/ancova-in-r/'
        self.notes      = _notes

    def _set_expected(self):
        e             = ExpectedResultsSPM1D()
        e.STAT        = 'F'
        e.z           = 218.629
        e.df          = (2, 41)
        e.p           = 1.35e-22
        e.tol.z       = 0.001
        e.tol.df      = 1e-05
        e.tol.p       = 1e-23
        self.expected = e

    def _set_params(self):
        self.params                   = ParametersSPM1D()
        self.params.testname          = 'ancova'
        self.params.args              = self.y, self.x
        self.params.kwargs            = dict(cov_model='iid')
        self.params.inference_args    = (0.05,)
        self.params.inference_kwargs4 = dict()
        self.params.inference_kwargs5 = dict(method='param')
