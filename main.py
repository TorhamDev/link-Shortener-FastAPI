from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from models import Link
from validations import link_validation
from utils import generate_short_link
from starlette.responses import RedirectResponse

app = FastAPI()


class LinkData(BaseModel):
    address: str


@app.post("/generate")
async def generate(link: LinkData, request: Request):

    if not link_validation(link.address):
        raise HTTPException(status_code=400, detail="Invalid link address")
    else:
        random_link = generate_short_link(link.address)

    short_link = Link(address=link.address, short_link=random_link)
    short_link.save()

    return {"link": f"{request.client.host}/{random_link}"}


@app.get("/{link}")
async def root(link: str):

    redirect_link = Link.select().where(Link.short_link == link)

    if redirect_link.exists():
        return RedirectResponse(url=redirect_link[0].address)
    else:
        raise HTTPException(status_code=400, detail="Short url doesn't exist")
