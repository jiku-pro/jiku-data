
'''
The data package checks only its data.

Every dataset must be discoverable, must load, and must carry finite
numerical arguments and an expected-results record.  Whether a statistics
package reproduces the expected results is that package's test, not this one:
spm1d keeps its own sweep over these datasets in its own repository, and
nothing here imports spm1d.
'''

import sys

import numpy as np
import pytest

import jikudata as jd


DATASETS = list( jd.datasets.iter_all() )


def test_datasets_are_discovered():
    assert len( DATASETS ) > 100
    names = [d.name for d in DATASETS]
    assert len( names ) == len( set(names) ), 'duplicate dataset names'


@pytest.mark.parametrize( 'dataset', DATASETS, ids=lambda d: d.name )
def test_dataset_loads_with_finite_arguments(dataset):
    if dataset.params is None:                # a data-only entry with no analysis
        assert dataset.expected is None
        return
    args = dataset.params.args
    assert len( args ) > 0
    for a in args:
        x = np.asarray( a, dtype=float )
        assert x.size > 0
        assert np.isfinite( x ).all(), f'{dataset.name}: non-finite values'
    assert dataset.expected is not None
    assert dataset.dim in (0, 1, 2)


def test_loading_every_dataset_imports_no_statistics_package():
    assert 'spm1d' not in sys.modules


@pytest.mark.parametrize( 'dataset', DATASETS, ids=lambda d: d.name )
def test_every_dataset_has_a_repr(dataset):
    '''print( dataset ) must work for every entry, data-only ones included.'''
    s = repr( dataset )
    assert dataset.name in s
