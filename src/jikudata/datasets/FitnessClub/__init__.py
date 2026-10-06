
import os
import numpy as np
from ... _cls import _Dataset, ExpectedResultsSPM1D, ParametersSPM1D



class FitnessClub(_Dataset):

    def _set_attrs(self):
        self.www        = 'https://support.sas.com/documentation/cdl/en/statug/63033/HTML/default/viewer.htm#statug_cancorr_sect020.htm'

    def _set_expected(self):
        e             = ExpectedResultsSPM1D()
        #  SAS PROC CANCORR reports the likelihood ratio (Wilks' lambda,
        #  1 - r2 = 0.7321) with its F, exact for one predictor:
        #  F = r2 / (1 - r2) * (J - 1 - I) / I = 1.95 on (3, 16) df, p = 0.1620.
        #  spm1d v0.5 reports that F;  the earlier expectation here was the
        #  Bartlett chi-square 5.1458 (df 3, p 0.1614), still available as
        #  "spm.fit.wilks_x2".
        e.STAT        = 'F'
        e.z           = 1.95185
        e.df          = (3, 16)
        e.p           = 0.161979
        e.tol.z       = 0.0001
        e.tol.df      = 1e-05
        e.tol.p       = 0.0001
        self.expected = e

    def _set_params(self):
        self.params                   = ParametersSPM1D()
        self.params.testname          = 'cca'
        self.params.args              = self.y, self.x
        self.params.inference_args    = (0.05,)
        self.params.inference_kwargs4 = dict()
        self.params.inference_kwargs5 = dict(method='param')
        
        # if self._spm_version == 4:
        #     self.params.inference_kwargs = dict()
        # else:
        #     self.params.inference_kwargs = dict(method='param')


