from re import match
from fastapi import HTTPException


def link_validation(link: str) -> bool:

    url_http_https = "^https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$"
    url_no_http_https = "^[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$"

    if match(url_http_https, link):
        return True
    elif match(url_no_http_https, link):
        return True
    else:
        raise HTTPException(status_code=400, detail="Invalid link address")
