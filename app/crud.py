"""
Module for handling mission-related database operations.

This module includes functions to create, retrieve, and search for missions
in the database using SQLAlchemy ORM. It provides basic CRUD operations
for interacting with mission data.

Functions:
    - create_mission: Creates a new mission in the database.
    - get_missions: Retrieves a list of missions with pagination support.
    - get_mission_by_name: Retrieves a mission by its name.
"""
from sqlalchemy.orm import Session
from . import models, schemas


def create_mission(db: Session, mission: schemas.MissionCreate):
    """
    Creates a new mission and adds it to the database.

    Args:
        db (Session): The database session.
        mission (schemas.MissionCreate): The mission data to be created.

    Returns:
        models.Mission: The created mission object.
    """
    db_mission = models.Mission(**mission.dict())
    db.add(db_mission)
    db.commit()
    db.refresh(db_mission)
    return db_mission


def get_missions(db: Session, skip: int = 0, limit: int = 10):
    """
    Retrieves a list of missions from the database with pagination.

    Args:
        db (Session): The database session.
        skip (int, optional): The number of records to skip. Defaults to 0.
        limit (int, optional): The maximum number of records to return. Defaults to 10.

    Returns:
        list: A list of mission objects.
    """
    return db.query(models.Mission).offset(skip).limit(limit).all()


def get_mission_by_name(db: Session, name: str):
    """
    Retrieves a mission from the database by its name.

    Args:
        db (Session): The database session.
        name (str): The name of the mission.

    Returns:
        models.Mission or None: The mission object if found, otherwise None.
    """
    return db.query(models.Mission).filter(models.Mission.name == name).first()
