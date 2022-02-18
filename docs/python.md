# Python

## Conda setup

```bash
conda create --name FooBarEnv python==3.8
conda activate FooBarEnv
conda install nb_conda_kernels # automatically install kernels
pip install poetry
poetry config virtualenvs.create false
poetry install --no-root
# deprecated by nb_conda_kernels => ipython kernel install --name "FooBarEnv"
```

## How to auto-format width for `pd.ExcelWriter()`

See: https://stackoverflow.com/a/61617835

```python
for column in df:
    column_length = max(df[column].astype(str).map(len).max(), len(column))
    col_idx = df.columns.get_loc(column)
    writer.sheets[sheet_name].set_column(col_idx, col_idx, column_length)
```

## What is the difference between `list(dict)` and `dict.keys()`

The difference is that `list(dict)` returns a copy and `dict.keys()` returns a
view of the original keys. If you modify the keys using `dict.keys()` they are
modified in the original dict as well. 

> Calling foo.keys() will return a dictionary view object. It supports
operations like membership test and iteration, but its contents are not
independent of the original dictionary – it is only a view.

See: https://stackoverflow.com/a/31837536

## How to do a basic setup for `logging` setup

```python
import logging
import sys

logging.basicConfig(
    stream=sys.stdout,
    format="%(asctime)-23s %(levelname)-8s %(name)-10.10s %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger()
```

## How to add logs

Add this to `pyproject.toml`

```python
[tool.pytest.ini_options]
log_cli = true
log_cli_level = "INFO"
log_cli_format = "%(asctime)s [%(levelname)8s] %(message)s (%(filename)s:%(lineno)s)"
log_cli_date_format = "%Y-%m-%d %H:%M:%S"
```