from re import match
from fastapi import HTTPException
from constants import WITH_HTTP, WITH_HTTPS


def link_validation(link: str) -> bool:
    """
    Validate user input link to see if a real url has been entered or not

    params : link : user input link

    return : True, False or HTTPException
    """

    if match(WITH_HTTPS, link):
        return True
    elif match(WITH_HTTP, link):
        return True
    else:
        raise HTTPException(status_code=400, detail="Invalid link address")
