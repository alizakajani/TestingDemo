import pytest

# continuous integration - test code everytime something new is added w/ Travis-CI
@pytest.mark.parametrize("a, b, expected", [
	(2, 3, 5),
	(3, 7, 10),
	(-2, 5, 3),
	(2, 10, 12),
	(0.1, 0.2, 0.3)
	])
def test_add(a, b, expected):
	from calculate import add
	result = add(a, b)
	assert result == pytest.approx(expected)

@pytest.mark.parametrize("a, b, expected", [
	(2, 3, -1),
	(7, 3, 4),
	(-2, 5, -7),
	(10, 2, 8)
	])
def test_subtract(a, b, expected):
	from calculate import subtract
	result = subtract(a, b)
	assert result == expected
