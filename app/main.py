from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, crud, schemas, database
from .api import spacex

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


@app.post("/missions/")
def create_mission(
    mission: schemas.MissionCreate, db: Session = Depends(get_db)
):
    # Check if mission already exists
    existing_mission = crud.get_mission_by_name(db, mission.name)
    if existing_mission:
        raise HTTPException(status_code=400, detail="Mission already exists")

    # New mission
    new_mission = crud.create_mission(db=db, mission=mission)
    return new_mission


@app.get("/spacex-launches/")
def spacex_launches():
    launches = spacex.get_spacex_launches()
    if launches:
        return launches
    else:
        raise HTTPException(
            status_code=404, detail="SpaceX launches not found!"
        )
