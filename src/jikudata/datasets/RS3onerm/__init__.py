
import os
import numpy as np
from ... _cls import _Dataset, ExpectedResultsListSPM1D, ParametersSPM1D



class RS3onerm(_Dataset):

    def _set_attrs(self):
        self.www        = 'https://real-statistics.com/anova-repeated-measures/two-between-subjects-factors-one-within-subjects-factor/'
        self.notes      = (
            "Real Statistics, 'Three Factor (2B+1W) Repeated Measures Anova', Example 1. "
            'A = age (young, old), B = gender (male, female), C = day (1-4; repeated measures).  nB < nC.'
            )

    def _set_expected(self):
        z             = (0.079827, 6.833292, 0.826402, 0.146119, 3.917512, 2.486373, 1.494455)
        df            = ((1, 36), (1, 36), (3, 108), (1, 36), (3, 108), (3, 108), (3, 108))
        p             = (0.77915, 0.012981, 0.482113, 0.704519, 0.010658, 0.06446, 0.220183)
        e             = ExpectedResultsListSPM1D('F', z, df, p)
        e.tol.z       = 0.001
        e.tol.df      = 1e-05
        e.tol.p       = 0.001
        self.expected = e

    def _set_params(self):
        self.params                   = ParametersSPM1D()
        self.params.testname          = 'anova3onerm'
        self.params.args              = self.y, self.x
        self.params.inference_args    = (0.05,)
        self.params.inference_kwargs4 = dict()
        self.params.inference_kwargs5 = dict(method='param')
