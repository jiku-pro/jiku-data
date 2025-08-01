
import os,pathlib
import datetime


version_str  = '0.1.7'



dir0         = pathlib.Path( __file__ ).parent.parent
date_str     = str( datetime.date.today() )








# update __init__.py
fpath = os.path.join(dir0, 'src', 'jikudata', '__init__.py')
with open(fpath, 'r') as f:
    lines = f.readlines()
    for i,line in enumerate(lines):
        if line.startswith('__version__'):
            break
    lines[i] = f"__version__ = '{version_str}'  # {date_str}\n"
with open(fpath, 'w') as f:
    f.writelines( lines )



# update pyproject.toml
fpath = os.path.join(dir0, 'pyproject.toml')
with open(fpath, 'r') as f:
    lines = f.readlines()
    for i,line in enumerate(lines):
        if line.startswith('version'):
            break
    lines[i] = f'version         = "{version_str}"\n'
with open(fpath, 'w') as f:
    f.writelines( lines )




# update README.md
fpath = os.path.join(dir0, 'README.md')
with open(fpath, 'r') as f:
    lines = f.readlines()
    for i,line in enumerate(lines):
        if line.startswith('![version]'):
            break
    lines[i] = f"![version](https://img.shields.io/badge/version-{version_str}-blue)\n"
with open(fpath, 'w') as f:
    f.writelines( lines )

