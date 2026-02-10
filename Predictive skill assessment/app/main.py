from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routes import router

app = FastAPI(title="Performance Forecasting")

# Mount the static directory to serve CSS, JS, and Images
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Include the page routes
app.include_router(router)
