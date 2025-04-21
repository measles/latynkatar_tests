"""Set some common parameters for all tests and add common fixtures"""

from pytest_metadata.plugin import metadata_key
from pytest_randomly import default_seed


def pytest_html_report_title(report):
    """Set title for HTML report"""
    report.title = "Łatynkatar site test"


def pytest_configure(config):
    """Set configuration to add values to Environment section of HTML report"""
    config.stash[metadata_key]["Randomly seed"] = default_seed
