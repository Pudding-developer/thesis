from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()

# Locate the templates folder relative to where the app runs
templates = Jinja2Templates(directory="app/templates")

@router.get("/")
async def login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@router.get("/dashboard")
async def dashboard(request: Request):
    return templates.TemplateResponse("studentDB.html", {"request": request})

@router.get("/studentDB")
async def student_db(request: Request):
    return templates.TemplateResponse("studentDB.html", {"request": request})

@router.get("/performance_overview")
async def performance_overview(request: Request):
    return templates.TemplateResponse("performance review.html", {"request": request})

@router.get("/learning_outcome_alignment")
async def learning_outcome_alignment(request: Request):
    return templates.TemplateResponse("LOA.html", {"request": request})

@router.get("/signup")
async def signup(request: Request):
    return templates.TemplateResponse("signup.html", {"request": request})

@router.get("/instructor_dashboard")
async def instructor_dashboard(request: Request):
    return templates.TemplateResponse("intructorDB.html", {"request": request})
    