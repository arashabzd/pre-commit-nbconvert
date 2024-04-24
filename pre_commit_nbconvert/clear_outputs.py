import argparse

from nbconvert import NotebookExporter
from nbconvert.nbconvertapp import NbConvertApp
from nbconvert.writers import FilesWriter
from traitlets.config import Config


def parse_args(args=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--output-dir", type=str, default="", dest="output_dir")
    parser.add_argument("filepath", type=str)
    args = parser.parse_args(args)
    return args


def parse_config(args):
    c = Config()
    c.NbConvertApp.use_output_suffix = False
    c.NotebookExporter.preprocessors = [
        "nbconvert.preprocessors.ClearOutputPreprocessor",
        "nbconvert.preprocessors.RegexRemovePreprocessor",
        "nbconvert.preprocessors.ClearMetadataPreprocessor",
    ]
    c.RegexRemovePreprocessor.patterns = ["\s*\Z"]
    c.FilesWriter.build_directory = args.output_dir
    return c


def main(args=None):
    args = parse_args(args)
    c = parse_config(args)
    app = NbConvertApp(config=c)
    app.exporter = NotebookExporter(config=c)
    app.writer = FilesWriter(config=c)
    app.convert_single_notebook(args.filepath)


if __name__ == "__main__":
    raise SystemExit(main())
