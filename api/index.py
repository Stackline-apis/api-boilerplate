from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv
from api.email_validator import router as email_router


load_dotenv()

app = FastAPI(
    title=os.getenv("API_NAME", "Stackline API"),

app.include_router(email_router)
    description=os.getenv("API_DESCRIPTION", "A Stackline utility API"),
    version=os.getenv("API_VERSION", "1.0.0"),
    docs_url="/docs",
    redoc_url="/redoc",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── Health & Root ──────────────────────────────────────────────────────────────

@app.get("/", tags=["Health"])
async def root():
    return {
        "status": "ok",
        "api": os.getenv("API_NAME", "Stackline API"),
        "version": os.getenv("API_VERSION", "1.0.0"),
        "docs": "/docs",
    }

@app.get("/health", tags=["Health"])
async def health():
    return {"status": "healthy"}

# ── Your API logic goes below this line ────────────────────────────────────────
# Replace this example endpoint with your actual API endpoints.

@app.get("/example", tags=["Example"])
async def example():
    """Example endpoint — replace with your API logic."""
    return {"message": "Replace this with your API logic"}
