import pytest

from rooki.client import Rooki


@pytest.fixture(scope="session")
def rooki():
    rooki = Rooki(mode="async", verify=False, output_dir='/tmp/rooki')
    return rooki
