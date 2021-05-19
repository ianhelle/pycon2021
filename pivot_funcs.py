"""Custom pivot functions."""

import urllib

def split_url(url: str) -> dict:
    """Split url into component parts."""
    return urllib.parse.urlparse(url)._asdict()


def is_https(url: str) -> bool:
    """Return true if URL is https."""
    url_comps = split_url(url)
    return url_comps.get("scheme", "").casefold() == "https"
