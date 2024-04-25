# pre-commit-nbconvert

This pre-commit hook lets you:

1. Store notebook reports into html/markdown format.
2. Clear outputs and delete empty cells from notebooks.

This helps to remove notebook outputs from git repository while saving the output into accessible formats as reports.

## Dependencies

The only dependency is [nbconvert](https://nbconvert.readthedocs.io/en/latest/index.html).

```bash
pip install nbconvert
```

## Usage

Add this to your `.pre-commit-config.yaml`.

```yaml
-   repo: https://github.com/arashabzd/pre-commit-nbconvert
    rev: "0.0.1"
    hooks:
    -   id: convert-notebooks
        args: [--format=html, --output-dir=reports/html]
    -   id: clear-notebook-outputs
```

Available format options are `html` and `markdown`. Set `--output-dir` otherwise reports will generate in the same place as your notebooks. Optionally add output-dir to your `.gitignore`.

Dont forget to run `pre-commit install`.
