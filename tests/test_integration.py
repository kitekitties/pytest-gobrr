import pytest
from calculator.calculator import Calculator


@pytest.fixture
def calculator():
    """Provide a calculator instance."""
    return Calculator()


class TestIntegration:
    """Integration tests for calculator operations."""

    def test_calculator_operations(self, calculator):
        """Test a sequence of calculator operations."""
        # First add two numbers
        result = calculator.add(5, 3)
        # Then multiply by 2
        result = calculator.multiply(result, 2)
        # Then subtract 4
        result = calculator.subtract(result, 4)
        # Final result should be 12
        assert result == 12

    @pytest.mark.slow
    def test_complex_calculation(self, calculator):
        """A more complex test that might be slow."""
        result = 0
        # Perform many calculations
        for i in range(1, 10):
            result = calculator.add(result, i)
            result = calculator.multiply(result, 2)

        assert result == 8960


# Demonstrate using test fixtures with different scopes
@pytest.fixture(scope="module")
def module_calculator():
    """Module-scoped calculator fixture."""
    print("\nCreating module calculator")
    calc = Calculator()
    yield calc
    print("\nDestroying module calculator")


def test_module_fixture1(module_calculator):
    """Test using module-scoped fixture."""
    assert module_calculator.add(1, 2) == 3


def test_module_fixture2(module_calculator):
    """Another test using the same module-scoped fixture."""
    assert module_calculator.multiply(2, 3) == 6
