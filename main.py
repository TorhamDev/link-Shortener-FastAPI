from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from models import Link
from validations import link_validation
from utils import create_short_link_record
from starlette.responses import RedirectResponse

app = FastAPI()


class LinkData(BaseModel):
    address: str


@app.post("/generate")
async def generate(link: LinkData, request: Request):

    link_address = link.address
    link_validation(link_address)
    random_link = create_short_link_record(link_address)

    return {"link": f"{request.client.host}/{random_link}"}


@app.get("/{link}")
async def root(link: str):

    redirect_link = Link.select().where(Link.short_link == link)

    if redirect_link.exists():
        return RedirectResponse(url=redirect_link[0].address)
    else:
        raise HTTPException(status_code=400, detail="Short url doesn't exist")
