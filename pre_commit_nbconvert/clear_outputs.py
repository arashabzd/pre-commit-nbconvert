import argparse

from nbconvert.nbconvertapp import NbConvertApp
from nbconvert.writers.files import FilesWriter
from traitlets.config import Config


def parse_args(args=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--output-dir", type=str, default="", dest="output_dir")
    parser.add_argument("paths", nargs="+", default=[])
    args = parser.parse_args(args)
    return args


def config_app(paths=[], output_dir=""):
    c = Config()
    c.NbConvertApp.export_format = "notebook"
    c.NbConvertApp.notebooks = paths
    c.NbConvertApp.recursive_glob = True
    c.NbConvertApp.use_output_suffix = False
    c.NotebookExporter.preprocessors = [
        "nbconvert.preprocessors.ClearOutputPreprocessor",
        "nbconvert.preprocessors.RegexRemovePreprocessor",
        "nbconvert.preprocessors.ClearMetadataPreprocessor",
    ]
    c.RegexRemovePreprocessor.patterns = ["\s*\Z"]
    c.FilesWriter.build_directory = output_dir
    app = NbConvertApp(config=c)
    app.writer = FilesWriter(config=c)
    return app


def clear_outputs(paths, output_dir=None):
    app = config_app(paths, output_dir)
    app.convert_notebooks()


def main(args=None):
    args = parse_args(args)
    clear_outputs(args.paths, args.output_dir)


if __name__ == "__main__":
    raise SystemExit(main())
