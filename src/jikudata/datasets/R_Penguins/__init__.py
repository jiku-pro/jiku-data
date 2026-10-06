
from ... _cls import _Dataset, ExpectedResultsListSPM1D, ParametersSPM1D


_notes = '''
Palmer penguins (R "datasets::penguins", CC0;  Horst, Hill & Gorman 2020), the
333 complete cases:  bill length (mm), bill depth (mm), flipper length (mm) and
body mass (g), by SPECIES (0 Adelie, 1 Chinstrap, 2 Gentoo), SEX (0 female,
1 male) and YEAR (0 2007, 1 2008, 2 2009).  Unbalanced.  Effects in order:
SPECIES, SEX, YEAR, SPECIES:SEX, SPECIES:YEAR, SEX:YEAR, SPECIES:SEX:YEAR.

Expected values follow from the Wilks' lambda values reported by
R's car::Anova( lm( cbind(...) ~ species * sex * year ), type=3, test='Wilks' ):
0.01392, 0.36339, 0.81672, 0.88040, 0.86202, 0.98046 and 0.95416, through
Rao's F approximation (the F that car::Anova prints), with c = 4 responses,
the effect's df (2, 1, 2, 2, 4, 2, 4) and df_e = 315.  Tolerances cover the
rounding of lambda to five decimals, which for the species effect
(lambda = 0.014) is a wide band on F.
'''


class R_Penguins(_Dataset):

    def _set_attrs(self):
        self.cite       = 'Gorman, K. B., Williams, T. D., & Fraser, W. R. (2014). Ecological sexual dimorphism and environmental variability within a community of Antarctic penguins (genus Pygoscelis). PLoS ONE, 9(3), e90081.'
        self.www        = 'https://search.r-project.org/R/refmans/datasets/html/penguins.html', 'https://allisonhorst.github.io/palmerpenguins/'
        self.notes      = _notes

    def _set_expected(self):
        z             = (583.11192, 136.64542, 8.30938, 5.12939, 2.96879, 0.77341, 0.9227)
        df            = ((8, 624.0), (4, 312.0), (8, 624.0), (8, 624.0), (16, 953.813371), (8, 624.0), (16, 953.813371))
        p             = (9.06446e-284, 2.62744e-67, 9.68724e-11, 3.29848e-06, 7.59939e-05, 0.626365, 0.542484)
        e             = ExpectedResultsListSPM1D('F', z, df, p)
        e.tol.z       = 0.1
        e.tol.df      = 1e-5
        e.tol.p       = 0.0002
        self.expected = e

    def _set_params(self):
        self.params                   = ParametersSPM1D()
        self.params.testname          = 'manova3'
        self.params.args              = self.y, self.x
        self.params.inference_args    = (0.05,)
        self.params.inference_kwargs4 = dict()
        self.params.inference_kwargs5 = dict(method='param')
