
from ... _cls import _Dataset, ExpectedResultsListSPM1D, ParametersSPM1D


_notes = '''
Plastic film data, Krzanowski (1998, p. 381), as typed in the example of R's
"summary.manova" help page:  tear resistance, gloss and opacity of 20 film
samples, by extrusion rate (low, high) and amount of additive (low, high),
five samples per cell.  Effects in order:  RATE, ADDITIVE, RATE:ADDITIVE.

Expected values follow from the Wilks' lambda values that R reports,
0.38186, 0.52303 and 0.77711, through Bartlett's chi-square approximation,
X2 = -(df_e - (c - I + 1)/2) ln(lambda), with c = 3 responses, I = 1 df per
effect and df_e = 16.  R's own p values use an F approximation (0.003034,
0.024745, 0.301782) and are not compared.  Tolerances cover the rounding of
lambda to five decimals.
'''


class Krzanowski1998plastic(_Dataset):

    def _set_attrs(self):
        self.cite       = 'Krzanowski, W. J. (1998). Principles of Multivariate Analysis. A User\'s Perspective. Oxford University Press.'
        self.www        = 'https://stat.ethz.ch/R-manual/R-devel/library/stats/html/summary.manova.html'
        self.notes      = _notes

    def _set_expected(self):
        z             = (13.959168, 9.397689, 3.656514)
        df            = ((1, 3), (1, 3), (1, 3))
        p             = (0.00296126, 0.0244451, 0.301023)
        e             = ExpectedResultsListSPM1D('X2', z, df, p)
        e.tol.z       = 0.0004
        e.tol.df      = 1e-5
        e.tol.p       = 3e-05
        self.expected = e

    def _set_params(self):
        self.params                   = ParametersSPM1D()
        self.params.testname          = 'manova2'
        self.params.args              = self.y, self.x
        self.params.inference_args    = (0.05,)
        self.params.inference_kwargs4 = dict()
        self.params.inference_kwargs5 = dict(method='param')
