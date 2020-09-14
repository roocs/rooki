import pytest

from rooki.client import Rooki


@pytest.fixture(scope="session")
def rooki():
    rooki = Rooki(mode='sync', verify=False)
    return rooki
