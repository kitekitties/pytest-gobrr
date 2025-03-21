import pytest
from calculator.calculator import Calculator


class TestCalculator:
    """Test suite for the Calculator class."""

    def setup_method(self):
        """Set up test fixtures."""
        self.calc = Calculator()

    def test_add(self):
        """Test add method."""
        assert self.calc.add(1, 2) == 3
        assert self.calc.add(-1, 1) == 0
        assert self.calc.add(-1, -1) == -2

    def test_subtract(self):
        """Test subtract method."""
        assert self.calc.subtract(3, 2) == 1
        assert self.calc.subtract(1, 1) == 0
        assert self.calc.subtract(-1, -1) == 0

    def test_multiply(self):
        """Test multiply method."""
        assert self.calc.multiply(3, 2) == 6
        assert self.calc.multiply(0, 5) == 0
        assert self.calc.multiply(-1, -1) == 1

    def test_divide(self):
        """Test divide method."""
        assert self.calc.divide(6, 2) == 3
        assert self.calc.divide(0, 5) == 0
        assert self.calc.divide(-1, -1) == 1

    def test_divide_by_zero(self):
        """Test division by zero raises ValueError."""
        with pytest.raises(ValueError) as excinfo:
            self.calc.divide(1, 0)
        assert "Cannot divide by zero" in str(excinfo.value)


# Demonstrate parameterized tests
@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (0, 0, 0),
    (-1, 1, 0),
    (0.1, 0.2, 0.3),
])
def test_add_parameterized(a, b, expected):
    """Test add method with different inputs."""
    calc = Calculator()
    result = calc.add(a, b)
    assert result == pytest.approx(expected)


# Skip test example
@pytest.mark.skip(reason="This is an example of a skipped test")
def test_advanced_feature():
    """This test is skipped."""
    assert False

import time

# Test with sleep to demonstrate spans
def test_with_spans(spans):
    """Test with sleep to demonstrate spans in Buildkite Test Analytics."""
    with spans.measure('sleep', 'Short sleep'):
        time.sleep(0.5)
        assert True
    with spans.measure('sleep', 'Long sleep'):
        time.sleep(10)
        assert True
    with spans.measure('sleep', 'Quick sleep'):
        time.sleep(0.2)
        assert True

# XFail test example
@pytest.mark.xfail(reason="This test is expected to fail")
def test_feature_in_progress():
    """This test is expected to fail."""
    assert False
