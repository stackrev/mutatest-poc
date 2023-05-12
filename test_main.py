""" Mutatest PoC.

Install: pytest, mutatest.
Python: 3.9+
Run: mutatest -s ./test_main.py -t "pytest" -r 314
"""
import pytest

# Testsuite
# See: https://mutatest.readthedocs.io/en/latest/mutants.html
class TestPoc():
    # Should be flagged by mutatest.
    def test_always_passes(self):
        assert True

    # Negative test, skip. Drops coverage.
    @pytest.mark.skip(reason="For failure only!")
    def test_always_fails(self):
        assert False

    # AugAssign
    def test_aa(self):
        x = 1
        y = 2
        x += y
        assert x == 3

    # BinOp
    def test_bb(self):
        x = 1
        y = 2
        x = y + y - x
        assert x == 3

    # BoolOp
    def test_bl(self):
        x = 1
        y = 2
        if y % 2 == 0:
            x = 'ok'
        assert x == 'ok'

    # Slices
    def test_su(self):
        x = [1,2,3,4]
        y = x[-2:0:-1]
        
        assert y == [3,2]

if __name__ == '__main__':
    pytest.main(["--cov"], plugins=[TestPoc()])