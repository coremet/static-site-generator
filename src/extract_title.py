import re

def extract_title(markdown):
    headers = []
    for line in markdown.splitlines():
        if re.match(r"^#{1} ", line):
            headers.append(line)
    if not headers:
        raise Exception("h1 header not found")
    return headers[0].lstrip("#").strip()