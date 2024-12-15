"""
FastAPI application for managing space missions and retrieving SpaceX launches.

This API allows users to:
- View and create space missions stored in a local database.
- Retrieve data on SpaceX launches from an external API.

Modules included:
- Models, CRUD operations, and database setup for local mission data.
- Integration with SpaceX API to fetch live launch data.

The app initializes the database tables on startup and provides an HTTP interface
for users to interact with the system.
"""

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, crud, schemas, database
from .api import spacex

app = FastAPI()


# Dependency to get database session
def get_db():
    """
    Dependency function to get a database session.
    This is used to interact with the database in FastAPI route handlers.

    Yields:
        Session: SQLAlchemy session object to interact with the database.
    """
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.on_event("startup")
def startup():
    """
    FastAPI startup event handler.
    This function creates all tables in the database upon server startup.
    """
    models.Base.metadata.create_all(bind=database.engine)


@app.get("/")
def read_root():
    """
    Root endpoint for the API.
    Returns a welcome message for the Space Nomad app.

    Returns:
        dict: A dictionary with a welcome message.
    """
    return {"message": "Welcome to Space Nomad!"}


@app.get("/missions/")
def get_missions(db: Session = Depends(get_db)):
    """
    Get all space missions stored in the database.

    Args:
        db (Session): The database session, provided by dependency injection.

    Returns:
        list: A list of missions from the database.
    """
    missions = crud.get_missions(db)
    return missions


@app.post("/missions/")
def create_mission(mission: schemas.MissionCreate, db: Session = Depends(get_db)):
    """
    Create a new space mission in the database.
    Checks if the mission already exists before creating a new one.

    Args:
        mission (schemas.MissionCreate): The mission data to be added.
        db (Session): The database session, provided by dependency injection.

    Raises:
        HTTPException: If the mission already exists in the database.

    Returns:
        dict: The newly created mission object.
    """
    # Check if mission already exists
    existing_mission = crud.get_mission_by_name(db, mission.name)
    if existing_mission:
        raise HTTPException(status_code=400, detail="Mission already exists")

    # New mission
    new_mission = crud.create_mission(db=db, mission=mission)
    return new_mission


@app.get("/spacex-launches/")
def spacex_launches():
    """
    Get a list of SpaceX launches by querying an external API.

    Returns:
        list: A list of SpaceX launches.

    Raises:
        HTTPException: If no SpaceX launches are found.
    """
    launches = spacex.get_spacex_launches()
    if launches:
        return launches

    raise HTTPException(status_code=404, detail="SpaceX launches not found!")
