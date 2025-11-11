# unit-testing-pytest

## Running main program (calculator)

```
//To set uv
uv init .
uv sync
```

```
//Running main program
uv run main.py
```

### Usage

1) Type operation (modulo, max, min, pow, abs, sqrt, is_odd, is_even, is_positive, is_negative)
2) Type numbers as prompted
3) Exit with 'exit'

## Unit testing (pytest)

Choose one of the options to run the tests with pytest

```
//-v (verbose) runs and shows each test
pytest -v
//-q (quiet) runs and shows only summary
pytest -q
//-x stops after first failure
pytest -x

```

## CI/CD Automation 

This repository includes a GitHub actions workflow that automatically builds and runs tests on ever push/pull, and fails the workflow if any tests fail