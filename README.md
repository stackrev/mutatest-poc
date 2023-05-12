# mutatest-poc

A small education test to showcase mutation analysis with python.
See: https://mutatest.readthedocs.io/en/latest/commandline.html

## Run

Run `mutatest -s ./test_main.py -t "pytest --conv"`

It will have 90% coverage, but all mutations would have survived. This means that the tests have **no value**. 

## Requirements

- `pytest`: test suite
- `pytest-conv`: coverage
- `mutatest`: mutation analysis
