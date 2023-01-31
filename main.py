from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from models import Link
from validations import link_validation
from utils import create_short_link_record, check_link_is_exsits, set_cashe
from starlette.responses import RedirectResponse, HTMLResponse
from database import redis_obj as redis

app = FastAPI()


class LinkData(BaseModel):
    address: str


@app.post("/generate")
async def generate(link: LinkData, request: Request):
    """
    This view is responsible for receiving links and creating short links

    params : link : user input link for shorting

    params : request : http request object

    retrun : short link in json or HTTPException
    """

    link_address = link.address

    cashe = redis.get(link_address)
    if cashe:
        return {"link": f"{request.client.host}/{cashe.decode()}"}

    else:
        is_exists = check_link_is_exsits(link_address)

        if is_exists != False:
            set_cashe(link_address, is_exists, 5)
            return {"link": f"{request.client.host}/{is_exists}"}

        else:
            link_validation(link_address)
            random_link = create_short_link_record(link_address)
            set_cashe(link_address, random_link, 60)
            return {"link": f"{request.client.host}/{random_link}"}



@app.get("/{link}")
async def redirect(link: str):
    """
    This function is responsible for checking the short link and
    redirect users to the path related to that short link

    params : short_link : user short link

    return : redirect user or HTTPException
    """

    redirect_link = Link.select().where(Link.short_link == link)

    if redirect_link.exists():
        return RedirectResponse(url=redirect_link[0].address)
    else:
        raise HTTPException(status_code=400, detail="Short url doesn't exist")


@app.get("/")
async def root():
    """
    Web site index
    """

    return HTMLResponse("Hello World!")
