import pytest


@pytest.fixture
def example_resource():
    print("SETUP: create resource")
    yield "resource"
    print("TEARDOWN: clean up resource")


def test_resource_is_available(example_resource):
    print("TEST: using resource")
    assert example_resource == "resource"
