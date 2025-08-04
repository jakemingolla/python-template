import pytest

@pytest.fixture
def example_fixture():
    return 1

def test_example(example_fixture):
    assert example_fixture == 1