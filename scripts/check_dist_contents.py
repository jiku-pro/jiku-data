'''
Verify that dataset payloads are actually present in a built distribution.

The wheel must contain every data file tracked under src/, otherwise
`pip install jiku-data` yields a package whose datasets cannot be loaded.

Usage:
    python scripts/check_dist_contents.py dist/jiku_data-*.whl [more dists...]

Accepts .whl and .tar.gz (sdist).  Exits non-zero on any missing file.
'''

import os
import pathlib
import subprocess
import sys
import tarfile
import zipfile


DATA_SUFFIXES = ('.csv', '.npz', '.h5', '.md')
ROOT          = pathlib.Path( __file__ ).parent.parent


def tracked_data_files():
    '''Data files tracked by git under src/, relative to src/.'''
    out = subprocess.run(
        ['git', 'ls-files', 'src'],
        cwd=ROOT, capture_output=True, text=True, check=True ).stdout.split()
    return { s.split('src/', 1)[1]  for s in out  if s.endswith(DATA_SUFFIXES) }


def dist_data_files(fpath):
    '''Data files inside a wheel or sdist, relative to the package root.'''
    fpath = str( fpath )
    if fpath.endswith('.whl'):
        names  = zipfile.ZipFile( fpath ).namelist()
        strip  = 0                      # wheels are already package-rooted
    elif fpath.endswith(('.tar.gz', '.tgz')):
        names  = tarfile.open( fpath ).getnames()
        strip  = 2                      # <name>-<version>/src/
    else:
        sys.exit( f'Unsupported distribution: {fpath}' )
    files = set()
    for s in names:
        if not s.endswith( DATA_SUFFIXES ):
            continue
        parts = s.split('/')[strip:]
        if parts and parts[0] == 'jikudata':
            files.add( '/'.join(parts) )
    return files


def main(argv):
    if not argv:
        sys.exit( __doc__ )
    expected = tracked_data_files()
    nfail    = 0
    for fpath in argv:
        found   = dist_data_files( fpath )
        missing = sorted( expected - found )
        name    = os.path.basename( fpath )
        if missing:
            nfail += 1
            print( f'FAIL  {name}: {len(missing)} of {len(expected)} data files missing' )
            for s in missing[:15]:
                print( f'          {s}' )
            if len(missing) > 15:
                print( f'          ... and {len(missing)-15} more' )
        else:
            print( f'OK    {name}: all {len(expected)} data files present' )
    if nfail:
        print( '\nDataset payloads are missing from the distribution.' )
        print( 'Check [tool.setuptools.package-data] in pyproject.toml.' )
    return 1 if nfail else 0


if __name__ == '__main__':
    sys.exit( main( sys.argv[1:] ) )
