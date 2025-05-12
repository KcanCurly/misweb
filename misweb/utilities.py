from urllib.parse import urlparse

def is_in_scope(url, scope):
    parsed_url = urlparse(url)
    return scope in parsed_url.netloc