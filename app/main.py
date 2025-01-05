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

from fastapi import FastAPI, Depends, HTTPException, BackgroundTasks
from sqlalchemy.orm import Session
from . import models, crud, schemas, database
from .api import spacex, make_api_request
# from .api.make_api_requests import make_api_request, parse_mission_data
from fastapi_utils.tasks import repeat_every

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
async def load_initial_data():
    """
    FastAPI startup event handler.
    This function creates all tables in the database upon server startup.
    """
    db = next(get_db())
    update_spacex_data(db)

@app.on_event("startup")
@repeat_every(seconds=3600)  # Runs every hour
def periodic_mission_update() -> None:
    db = next(get_db())
    update_spacex_data(db)


def update_spacex_data(db: Session):
    spacex_response = spacex.spacex_data # make_api_request(SPACEX_API_URL)
    if spacex_response:
        spacex_missions =  make_api_request.parse_mission_data(spacex_response)
        for mission in spacex_missions:
            crud.create_or_update_mission(db, mission)

@app.get("/")
def read_root():
    """
    Root endpoint for the API.
    Returns a welcome message for the Space Nomad app.

    Returns:
        dict: A dictionary with a welcome message.
    """
    return {"message": "Welcome to Space Nomad!"}

@app.post("/update-missions/")
def trigger_spacex_update(background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    """
    Trigger a manual update for SpaceX missions.
    Runs in the background to avoid blocking the request.
    """
    background_tasks.add_task(update_spacex_data, db)
    return {"message": "SpaceX missions update initiated."}

@app.get("/missions/")
def get_missions(
    db: Session = Depends(get_db),
    page: int = 1,
    size: int = 10,
    start_date: str = None,
    end_date: str = None,
    keyword: str = None,
    ):
    """
    Fetch missions with pagination and optional filtering.
    """
    missions = crud.get_filtered_missions(
        db, page, size, start_date, end_date, keyword
    )
    return {"missions": missions, "page": page, "size": size}

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
    launches = spacex.spacex_data
    if launches:
        return launches

    raise HTTPException(status_code=404, detail="SpaceX launches not found!")
