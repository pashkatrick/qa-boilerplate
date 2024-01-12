# qa-boilerplate

## particularity
there is a string in `pyproject.toml` 

```bash
addopts = "--clean-alluredir --alluredir allure_result --numprocesses 3 --retries 1 --retry-delay 3"
```
it reference to allure-pytest, pytest-xdist and pytest-retry libs and auto add flags to main command, like

```bash
pytest -s tests/test_first.py
```
or

```bash
pytest -s -k TestFirst
```


## included libs

```bash
allure-pytest
pydantic
pytest
pytest-retry
pytest-xdist
requests
ruff
soft-assert
```

## codestyle
To check the code style

```bash
ruff check .
```

To format the code

```bash
ruff format .
```

all of this setting up in `pyproject.toml`