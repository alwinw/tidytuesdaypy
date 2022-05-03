import logging
import os

log = logging.getLogger(__name__)


def get_github_pat() -> str:
    """
    Get the local user's GitHub Personal Access Token

    Extract the GitHub Personal Access Token (PAT) from the system environment for
    authenticated requests.
    """
    if "GITHUB_TOKEN" in os.environ and os.environ["GITHUB_TOKEN"]:
        log.debug("Using GITHUB_TOKEN from environment")
        return os.environ["GITHUB_TOKEN"]
    if "GITHUB_PAT" in os.environ and os.environ["GITHUB_PAT"]:
        log.debug("Using GITHUB_PAT from environment")
        return os.environ["GITHUB_PAT"]
    return ""


TT_REPO = "rfordatascience/tidytuesday"


def from_date(year, date):
    url = "https://api.github.com/repos/{}/contents/data/{}/{}"
    url.format(TT_REPO, year, date)
