
import os
import numpy as np
from ... _cls import _Dataset, ExpectedResultsListSPM1D, ParametersSPM1D



class RS3tworm(_Dataset):

    def _set_attrs(self):
        self.www        = 'https://real-statistics.com/anova-repeated-measures/one-between-subjects-factor-two-within-subjects-factors/'
        self.notes      = (
            "Real Statistics, 'Three Factor (1B+2W) Repeated Measures Anova', Example 1. "
            'A = group (G1-G3), B = test (T1-T4; repeated measures), C = hand (left, right; repeated measures).  nB != nC.'
            )

    def _set_expected(self):
        z             = (1.993896, 9.168953, 98.242719, 3.2112, 17.825533, 6.066639, 4.17852)
        df            = ((2, 18), (3, 54), (1, 18), (6, 54), (2, 18), (3, 54), (6, 54))
        p             = (0.165127, 5.3e-05, 0.0, 0.009049, 5.4e-05, 0.001232, 0.001605)
        e             = ExpectedResultsListSPM1D('F', z, df, p)
        e.tol.z       = 0.001
        e.tol.df      = 1e-05
        e.tol.p       = 0.001
        self.expected = e

    def _set_params(self):
        self.params                   = ParametersSPM1D()
        self.params.testname          = 'anova3tworm'
        self.params.args              = self.y, self.x
        self.params.inference_args    = (0.05,)
        self.params.inference_kwargs4 = dict()
        self.params.inference_kwargs5 = dict(method='param')
