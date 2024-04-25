import os
from tempfile import TemporaryDirectory

import nbformat

from pre_commit_nbconvert.clear_outputs import clear_outputs


def is_clear(nb_path):
    nb = nbformat.read(nb_path, as_version=4)
    with TemporaryDirectory() as tmpdir:
        clear_outputs([nb_path], tmpdir)
        nb_clear_path = os.path.join(tmpdir, os.path.basename(nb_path))
        nb_clear = nbformat.read(nb_clear_path, as_version=4)
    return nb == nb_clear
