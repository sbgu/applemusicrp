import os
import glob
from setuptools import setup
import platform
import py2exe


def find_data_files(source, target, patterns):
    # Stolen from py2exe docs :p
    """Locates the specified data-files and returns the matches
    in a data_files compatible format.

    source is the root of the source data tree.
        Use '' or '.' for current directory.
    target is the root of the target data tree.
        Use '' or '.' for the distribution directory.
    patterns is a sequence of glob-patterns for the
        files you want to copy.
    """
    if glob.has_magic(source) or glob.has_magic(target):
        raise ValueError("Magic not allowed in src, target")

    ret = {}

    for pattern in patterns:
        pattern = os.path.join(source, pattern)
        for filename in glob.glob(pattern):
            if os.path.isfile(filename):
                targetpath = os.path.join(
                    target, os.path.relpath(filename, source))
                path = os.path.dirname(targetpath)
                ret.setdefault(path, []).append(filename)

    return sorted(ret.items())


install_dependencies = ['based', 'pypresence', 'pywin32',
                        'pystray', 'pillow', 'psutil', 'dialite']

setup(
    options={'py2exe': {'compressed': True,
                        'compressed': 1,
                        "dist_dir": "dist/windows/"
                        }},
    windows=[{
        "script": "applemusicrp.py",
        "icon_resources": [(1, "assets/icon.ico")],
    }],    data_files=find_data_files('.', '', [
        'assets/*'
    ]),
    setup_requires=['py2exe', 'setuptools'],
    install_requires=install_dependencies
)
