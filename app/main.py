from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.core.config import settings

# Create FastAPI instance
app = FastAPI(
    title="Library Management System",
    description="A library management system built with FastAPI and SSR",
    version="1.0.0",
    debug=settings.debug
)

# Mount static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Setup Jinja2 templates
templates = Jinja2Templates(directory="app/templates")


# Home route with SSR
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "title": "Library Management"})


# Health check
@app.get("/health")
async def health_check():
    return {"status": "healthy", "message": "Library Management System is running"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.debug
    )
