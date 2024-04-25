import os
from tempfile import TemporaryDirectory

import nbformat

from pre_commit_nbconvert.clear_outputs import clear_outputs


def test_clear_outputs():
    nb_clear = nbformat.read("tests/notebooks/clear/notebook.ipynb", as_version=4)
    with TemporaryDirectory(dir="tests/notebooks/") as tmpdir:
        clear_outputs(["tests/notebooks/notebook.ipynb"], tmpdir)
        nb_path = os.path.join(tmpdir, "notebook.ipynb")
        nb = nbformat.read(nb_path, as_version=4)
    assert nb_clear == nb


if __name__ == "__main__":
    test_clear_outputs()
