from fastapi import FastAPI, Request
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory = "static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/")
async def root():
    return 'Hello, World!'


@app.get("/hello/{name}")
async def say_hello(request: Request, name: str):
    return templates.TemplateResponse("item.html", {"request": request, "name": name})

