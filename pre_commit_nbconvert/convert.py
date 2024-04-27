import argparse

from nbconvert.nbconvertapp import NbConvertApp
from nbconvert.writers.files import FilesWriter
from traitlets.config import Config

from pre_commit_nbconvert.utils import is_clear


def parse_args(args=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--format", type=str, default="html", dest="format")
    parser.add_argument("-o", "--output-dir", type=str, default="", dest="output_dir")
    parser.add_argument("paths", nargs="+", default=[])
    args = parser.parse_args(args)
    return args


def config_app(format, paths=[], output_dir=""):
    c = Config()
    preprocessors = [
        "nbconvert.preprocessors.RegexRemovePreprocessor",
        "nbconvert.preprocessors.ClearMetadataPreprocessor",
    ]
    c.NbConvertApp.export_format = format
    c.NbConvertApp.notebooks = paths
    c.NbConvertApp.recursive_glob = True
    c.NbConvertApp.use_output_suffix = False
    c.HTMLExporter.preprocessors = preprocessors
    c.MarkdownExporter.preprocessors = preprocessors
    c.NotebookExporter.preprocessors = preprocessors
    c.TemplateExporter.exclude_input = True
    c.TemplateExporter.exclude_input_prompt = True
    c.TemplateExporter.exclude_output_prompt = True
    c.RegexRemovePreprocessor.patterns = ["\s*\Z"]
    c.FilesWriter.build_directory = output_dir
    app = NbConvertApp(config=c)
    app.writer = FilesWriter(config=c)
    return app


def convert(format, paths, output_dir=None):
    paths = [path for path in paths if not is_clear(path)]
    if paths:
        app = config_app(format, paths, output_dir)
        app.convert_notebooks()


def main(args=None):
    args = parse_args(args)
    convert(args.format, args.paths, args.output_dir)


if __name__ == "__main__":
    raise SystemExit(main())
