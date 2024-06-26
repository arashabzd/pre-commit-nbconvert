# pre-commit-nbconvert

This pre-commit hook lets you:

1. Store notebook reports into `markdown` (default), `html`, and `pdf` format.
2. Clear outputs and delete empty cells from notebooks.

This helps to remove notebook outputs from git repository while saving the output into accessible formats as reports.

You can find report examples of the [sample notebook](tests/notebook.ipynb) in [reports](reports/) folder.

## Dependencies

To export `pdf` reports [Pandoc](https://pandoc.org/installing.html) and [TeX](https://nbconvert.readthedocs.io/en/latest/install.html#installing-tex) must be installed on your system.

## Usage

Add this to your `.pre-commit-config.yaml`.

```yaml
-   repo: https://github.com/arashabzd/pre-commit-nbconvert
    rev: "0.0.4"
    hooks:
    -   id: convert-notebooks
        args: [--format=markdown, --output-dir=reports, --no-code]
    -   id: clear-notebook-outputs
```

__`convert-notebooks` must be put before `clear-notebook-outputs`__.

Available format options are `markdown` (default), `html` and optionally `pdf`. Set `--output-dir` otherwise reports will generate in the same place as your notebooks. Optionally add output-dir to your `.gitignore`.

Dont forget to run `pre-commit install`.

## Why?

1. You can add a local pre-commit hook to clear outputs using nbconvert equivalent to command `jupyter nbconvert --clear-output`. The only problem is that this doesn't remove empty cells. For some reason `--RegexRemovePreprocessor.patterns="['\s*\Z']"` doesn't work in CLI when you export to notebook.
2. You can add a local pre-commit hook to convert notebooks to other formats using nbconvert equivalent to `jupyter nbconvert --to html ...`. The problem is using it while clearing output in pre-commit leads to overriding reports with empty notebook reports. The workaround used here is to override reports only if the notebook is not cleared.

More detailed explanation [here](https://arashabzd.github.io/posts/nbconvert-pre-commit/).
