# pre-commit-nbconvert

Simple pre-commit hooks for jupyter notebooks using nbconvert.
Currently there are 3 pre-commit hooks available:

1. `nbconvert`: Generic nbconvert command.
2. `nbconvert-to-html`: Export jupyter notebooks into html format.
3. `nbconvert-to-md`: Export jupyter notebooks into markdown format.
4. `nbconvert-clear-outputs`: Clear notebook outputs.

## Requirements

Install [`nbconvert`](https://nbconvert.readthedocs.io/en/latest/install.html) in your environment.

## Usage

Add the following to your `.pre-commit-config.yaml`.

```yaml
-   repo: https://github.com/arashabzd/pre-commit-nbconvert
    rev: v0.1.1
    hooks:
    -   id: nbconvert-to-html
        args: [--output-dir, reports/html]
    -   id: nbconvert-to-html
        args: [--output-dir, reports/md]
    -   id: nbconvert-clear-output
```

- By default html/markdown files will be saved in the same path as the notebooks. Configure `output-dir` to change the output directory.

- `nbconvert-to-html` must be placed before `nbvonvert-clear-outputs` otherwise notebook outputs won't be saved.
