from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, crud, schemas, database
from .api import nasa, spacex

app = FastAPI()


# Dependency to get database session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.on_event("startup")
def startup():
    # Create tables in database
    models.Base.metadata.create_all(bind=database.engine)


@app.get("/")
def read_root():
    return {"message": "Welcome to Space Nomad!"}


@app.get("/missions/")
def get_missions(db: Session = Depends(get_db)):
    missions = crud.get_missions(db)
    return missions