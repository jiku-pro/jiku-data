
import os
import numpy as np
from ... _cls import _Dataset, ExpectedResultsSPM1D, ParametersSPM1D


_notes = '''
Originally accessed from the following link (unavailable as of 2023-01-30):
http://www.pearsonhighered.com/assets/hip/gb/uploads/Mayers_IntroStatsSPSS_Ch14.pdf

Results verified in MATLAB using manova1, which reports Wilks' lambda as
Bartlett's chi-square:  X2 = 23.8481 with df = 4.  spm1d v0.5 reports Wilks'
lambda as Rao's F (exact here, I = 2), so the expectation is that chi-square
converted:  lambda = exp(-X2 / kappa) with kappa = df_e - (I - c + 1)/2 = 26.5
(df_e = 27, c = 2), then F = (1 - lambda^(1/s)) / lambda^(1/s) * df2 / df1 with
s = 2, df1 = I c = 4, df2 = 2 df_e - 2 = 52.  The chi-square itself remains
available as "spm.fit.wilks_x2".
'''

class AnimalDepression(_Dataset):

    def _set_attrs(self):
        self.www        = None
        self.notes      = _notes

    def _set_expected(self):
        e             = ExpectedResultsSPM1D()
        e.STAT        = 'F'
        e.z           = 7.38733
        e.df          = (4, 52)
        e.p           = 8.6511e-05
        e.tol.z       = 0.0001
        e.tol.df      = 1e-05
        e.tol.p       = 1e-08
        self.expected = e

    def _set_params(self):
        self.params                   = ParametersSPM1D()
        self.params.testname          = 'manova1'
        self.params.args              = self.y, self.x
        self.params.inference_args    = (0.05,)
        self.params.inference_kwargs4 = dict()
        self.params.inference_kwargs5 = dict(method='param')

