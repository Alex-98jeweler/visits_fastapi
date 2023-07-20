from fastapi import FastAPI

from src.visits.routers import router as visit_router


app = FastAPI()


app.include_router(visit_router)