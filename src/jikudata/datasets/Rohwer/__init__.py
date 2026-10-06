
from ... _cls import _Dataset, ExpectedResultsListSPM1D, ParametersSPM1D


_notes = '''
Rohwer data (Timm 1975;  R package "heplots", dataset "Rohwer"):  three
achievement scores (SAT, PPVT, Raven) for 69 kindergarten children, 37 of low
and 32 of high socioeconomic status (SES:  0 low, 1 high), with five
paired-associate learning-task scores as covariates (N, S, NS, NA, SS).  The
first column is the factor and the next five are the covariates;  the three
response columns follow.

The expected value follows from the Wilks' lambda for SES reported by
R's car::Anova( lm( cbind(SAT, PPVT, Raven) ~ SES + n + s + ns + na + ss ), test='Wilks' ),
0.62147 (Pillai 0.37853), through Rao's F, exact here with one df:
F(3, 60) = 12.1818, p = 2.507e-06, as R prints.  The tolerance covers the
rounding of lambda to five decimals.
'''


class Rohwer(_Dataset):

    def _set_attrs(self):
        self.cite       = 'Timm, N. H. (1975). Multivariate Analysis with Applications in Education and Psychology. Brooks/Cole.'
        self.www        = 'https://cran.r-project.org/web/packages/heplots/vignettes/HE_mmra.html', 'https://friendly.github.io/heplots/reference/Rohwer.html'
        self.notes      = _notes

    def _set_expected(self):
        z             = (12.18176,)
        df            = ((3, 60.0),)
        p             = (2.50682e-06,)
        e             = ExpectedResultsListSPM1D('F', z, df, p)
        e.tol.z       = 0.0003
        e.tol.df      = 1e-5
        e.tol.p       = 7e-10
        self.expected = e

    def _set_params(self):
        self.params                   = ParametersSPM1D()
        self.params.testname          = 'mancova'
        self.params.args              = self.y, self.x
        self.params.inference_args    = (0.05,)
        self.params.inference_kwargs4 = dict()
        self.params.inference_kwargs5 = dict(method='param')
