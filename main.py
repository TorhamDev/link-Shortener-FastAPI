from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from models import Link
from validations import link_validation
from utils import create_short_link_record, check_link_is_exists, set_cache
from starlette.responses import RedirectResponse
from database import redis_obj as redis
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles


app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


class LinkData(BaseModel):
    address: str


@app.post("/generate")
async def generate(link: LinkData, request: Request):
    """
    This view is responsible for receiving links and creating short links

    params : link : user input link for shorting

    params : request : http request object

    return : short link in json or HTTPException
    """

    link_address = link.address

    cache = redis.get(link_address)
    if cache:
        return {"link": f"{request.client.host}/{cache.decode()}"}

    is_exists = check_link_is_exists(link_address)

    if is_exists:
        set_cache(link_address, is_exists, 60)
        return {"link": f"{request.client.host}/{is_exists}"}

    link_validation(link_address)
    random_link = create_short_link_record(link_address)
    set_cache(link_address, random_link, 60)
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
async def root(request: Request):
    """
    Web site index
    """

    return templates.TemplateResponse("index.html", {"request": request})
