
import pytest

import jikudata as jd


# Auto-tested designs.  Keep this list in sync with the designs that are
# known to reproduce exactly across the supported spm1d versions.
TESTNAMES = ['ttest', 'ttest_paired', 'ttest2', 'anova1']


def _dataset_names():
    names = []
    for testname in TESTNAMES:
        names += jd.datasets.get_dataset_names( testname=testname )
    return sorted( set(names) )


@pytest.mark.parametrize( 'name', _dataset_names() )
def test_dataset(name):
    dataset = jd.get_dataset_by_name( name )
    if not dataset._autotest:
        pytest.skip( f'{name}: auto-testing disabled' )
    dataset.runtest( verbose=True, spm1d_version=None )
