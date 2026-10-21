
from ... _cls import _Dataset, ExpectedResultsListSPM1D, ParametersSPM1D


_notes = '''
Data: datarium::weightloss.  Twelve sedentary men completed four nine-week
trials in counterbalanced order (no intervention, diet only, exercise only,
diet and exercise), with weight loss scored at three time points in each,
so all three factors are repeated measures:  A = diet (0 no, 1 yes),
B = exercises (0 no, 1 yes), C = time (t1, t2, t3), S = participant.

Results: rstatix::anova_test(dv = score, wid = id, within = c(diet, exercises, time)),
as printed in the three-way repeated measures ANOVA section of
https://www.datanovia.com/en/lessons/repeated-measures-anova-in-r/ :
diet F(1, 11) = 6.021, exercises F(1, 11) = 58.928, time F(2, 22) = 110.942,
diet:exercises F(1, 11) = 75.356, diet:time F = 0.603, exercises:time
F(2, 22) = 20.826, diet:exercises:time F(2, 22) = 14.246.  The table prints
diet:time with Greenhouse-Geisser df (1.38, 15.17) and p = 0.501;  the
expectation here is the sphericity-assumed test the F values come from,
df (2, 22) and p = 0.556, hence cov_model="iid".

The data sets in datarium are dedicated to the public domain (CC0 1.0).
'''


class DatariumWeightloss(_Dataset):

    def _set_attrs(self):
        self.cite       = 'Kassambara, A. (2019) datarium: Data Bank for Statistical Analysis and Visualization. R package.'
        self.www        = 'https://cran.r-project.org/package=datarium', 'https://www.datanovia.com/en/lessons/repeated-measures-anova-in-r/'
        self.notes      = _notes

    def _set_expected(self):
        z             = (6.021, 58.928, 110.942, 75.356, 0.603, 20.826, 14.246)
        df            = ((1, 11), (1, 11), (2, 22), (1, 11), (2, 22), (2, 22), (2, 22))
        p             = (0.0320, 9.65e-06, 3.22e-12, 2.98e-06, 0.556, 8.41e-06, 1.07e-04)
        e             = ExpectedResultsListSPM1D('F', z, df, p)
        e.tol.z       = 0.001
        e.tol.df      = 1e-05
        e.tol.p       = 0.001
        self.expected = e

    def _set_params(self):
        self.params                   = ParametersSPM1D()
        self.params.testname          = 'anova3rm'
        self.params.args              = self.y, self.x
        self.params.kwargs            = dict(cov_model='iid')
        self.params.inference_args    = (0.05,)
        self.params.inference_kwargs4 = dict()
        self.params.inference_kwargs5 = dict(method='param')
