import os
import rooki.config as config


def test_load_configuration_allows_duplicate_env(monkeypatch):
    # Simulate a duplicate key environment by shadowing os.environ
    fake_env = {
        "__LMOD_REF_COUNT_GCC_VERSION": "8.5.0:1",
        # Pretend the same key appears twice – ConfigParser(strict=False) should accept
        "PATH": "/usr/bin",
    }

    # Monkeypatch os.environ so config.load_configuration sees it
    monkeypatch.setattr(os, "environ", fake_env)

    # This should not raise DuplicateOptionError
    config.load_configuration()

    # Ensure defaults were set
    assert config.CONFIG.get("service", "url") == "http://rook.dkrz.de/wps"

    # Ensure env values are accessible as defaults
    assert config.CONFIG.defaults()["path"] == "/usr/bin"
