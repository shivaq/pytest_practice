import pytest


@pytest.mark.run_these_please
def test_failing():
    assert (1, 2, 3) == (3, 2, 1)
