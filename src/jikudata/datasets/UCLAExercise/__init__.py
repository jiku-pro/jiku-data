
import os
import numpy as np
from ... _cls import _Dataset, ExpectedResultsListSPM1D, ParametersSPM1D



class UCLAExercise(_Dataset):

    def _set_attrs(self):
        self.www        = 'https://stats.oarc.ucla.edu/r/seminars/repeated-measures-analysis-with-r/'
        self.notes      = (
            'Data: https://stats.oarc.ucla.edu/wp-content/uploads/2016/02/exer.csv. '
            "Results: 'Exercise example', model 3: aov(pulse ~ exertype * diet * time + Error(id)). "
            'A = exercise type (rest, walking, running), B = diet (low fat, not low fat), '
            'C = time (1, 15, 30 min; repeated measures).  nB < nC.'
            )

    def _set_expected(self):
        z             = (47.9152, 14.5238, 31.7206, 4.6945, 20.9005, 2.9597, 4.7095)
        df            = ((2, 24), (1, 24), (2, 48), (2, 24), (4, 48), (2, 48), (4, 48))
        p             = (4.166e-09, 0.0008483, 1.662e-09, 0.019023, 4.992e-10, 0.06137, 0.00275)
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
