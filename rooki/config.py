import os
import configparser
import logging

ROOKI_HOME = os.path.abspath(os.path.dirname(__file__))
DEFAULT_CFG = os.path.join(ROOKI_HOME, "default.cfg")

RAW_OPTIONS = [
    ("logging", "format"),
]

CONFIG = None
LOGGER = logging.getLogger("ROOKI")


def get_config_value(section, option):
    """Get desired value from  configuration files
    :param section: section in configuration files
    :type section: string
    :param option: option in the section
    :type option: string
    :returns: value found in the configuration file
    """

    if not CONFIG:
        load_configuration()

    value = ""

    if CONFIG.has_section(section):
        if CONFIG.has_option(section, option):
            raw = (section, option) in RAW_OPTIONS
            value = CONFIG.get(section, option, raw=raw)

            # Convert Boolean string to real Boolean values
            if value.lower() == "false":
                value = False
            elif value.lower() == "true":
                value = True

    return value


def load_configuration(cfgfiles=None):
    """Load rooki configuration from configuration files.
    The later configuration file in the array overwrites configuration
    from the first.
    :param cfgfiles: list of configuration files
    """
    global CONFIG

    LOGGER.info("loading configuration")
    CONFIG = configparser.ConfigParser(os.environ)

    LOGGER.debug("setting default values")
    CONFIG.add_section("service")
    CONFIG.set("service", "url", "http://localhost:5000/wps")

    config_files = _get_default_config_files_location()
    if cfgfiles:
        config_files.extend(cfgfiles)

    if "ROOKI_CFG" in os.environ:
        config_files.append(os.environ["ROOKI_CFG"])

    loaded_files = CONFIG.read(config_files)
    if loaded_files:
        LOGGER.info("Configuration file(s) {} loaded".format(loaded_files))
    else:
        LOGGER.info("No configuration files loaded. Using default values")
    # dirty hack to set rook url on binder
    if "ROOK_URL" in os.environ:
        CONFIG.set("service", "url", os.environ["ROOK_URL"])
    if "ROOK_MODE" in os.environ:
        CONFIG.set("service", "mode", os.environ["ROOK_MODE"])
    if "ROOK_SSL_VERIFY" in os.environ:
        CONFIG.set("service", "ssl_verify", os.environ["ROOK_SSL_VERIFY"])


def _get_default_config_files_location():
    """Get the locations of the standard configuration files. These are
        1. `$ROOKI_HOME/default.cfg`
        2. `/etc/rooki.cfg`
        3. `$HOME/.rooki.cfg`
    :returns: configuration files
    :rtype: list of strings
    """
    LOGGER.debug("trying to estimate the default location")
    cfgfiles = [
        DEFAULT_CFG,
        "/etc/rooki.cfg",
    ]
    if "HOME" in os.environ:
        cfgfiles.append(os.path.join(os.environ["HOME"], ".rooki.cfg"))
    return cfgfiles
