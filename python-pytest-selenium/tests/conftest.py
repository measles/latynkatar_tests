from pytest_metadata.plugin import metadata_key
from pytest_randomly import default_seed


def pytest_html_report_title(report):
    report.title = "Łatynkatar site test"
    

def pytest_configure(config):
    config.stash[metadata_key]["Randomly seed"] = default_seed
