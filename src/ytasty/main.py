from fastapi import FastAPI

from ytasty.db.base import Base
from ytasty.db.database import engine
import ytasty.models

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/health")
def health():
    return {"status": "ok"}