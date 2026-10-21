
import os
import numpy as np
from ... _cls import _Dataset, ExpectedResultsListSPM1D, ParametersSPM1D



class DatariumPerformance(_Dataset):

    def _set_attrs(self):
        self.cite       = 'Kassambara, A. (2019) datarium: Data Bank for Statistical Analysis and Visualization. R package.'
        self.www        = 'https://cran.r-project.org/package=datarium'
        self.notes      = (
            'Data: datarium::performance. '
            'Results: aov(score ~ gender * stress * time + Error(id)). '
            'A = gender, B = stress (low, moderate, high), C = time (t1, t2; repeated measures).  nB > nC.'
            )

    def _set_expected(self):
        z             = (2.405773, 21.16635, 0.063027, 1.554212, 4.730123, 1.820635, 6.101118)
        df            = ((1, 54), (2, 54), (1, 54), (2, 54), (1, 54), (2, 54), (2, 54))
        p             = (0.12673, 1.6e-07, 0.802727, 0.220662, 0.034038, 0.171722, 0.004084)
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
