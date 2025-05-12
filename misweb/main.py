import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import argparse
import sys
import urllib3

urllib3.disable_warnings()

visited = set()

def is_in_scope(url, scope):
    parsed_url = urlparse(url)
    return scope in parsed_url.netloc

def crawl(url, scope):
    if url in visited:
        return
    visited.add(url)

    print(f"[+] Visiting: {url}")

    try:
        response = requests.get(url, timeout=5, verify=False)
        response.raise_for_status()
    except (requests.RequestException, KeyboardInterrupt):
        print(f"[-] Failed to fetch: {url}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    for a_tag in soup.find_all('a', href=True):
        link = urljoin(url, a_tag['href'])
        print(link)
        if is_in_scope(link, scope):
            crawl(link, scope)

def main():
    parser = argparse.ArgumentParser(description="Simple Python Web Crawler")
    parser.add_argument("url", help="Starting URL to crawl")
    parser.add_argument("in_scope", help="Domain name to keep crawling in-scope (e.g., example.com)")
    args = parser.parse_args()

    parsed = urlparse(args.url)
    if not parsed.scheme:
        print("[-] URL must include scheme (http:// or https://)")
        sys.exit(1)

    crawl(args.url, args.in_scope)