"""
Module for defining the Mission ORM model.

This module contains the definition of the `Mission` model, which represents
a mission in the database. It extends from SQLAlchemy's `Base` and defines the
structure of the "missions" table, including its columns and their types.
"""

from sqlalchemy import Column, Integer, String
from .database import Base


# pylint: disable=too-few-public-methods
class Mission(Base):
    """
    Represents a mission in the database.

    The `Mission` class maps to the "missions" table in the database and
    contains the following columns:
        - id: A unique identifier for the mission (Primary Key).
        - name: The name of the mission.
        - status: The current status of the mission (e.g., active, completed).
        - description: A brief description of the mission.

    Attributes:
        id (int): The mission's unique ID.
        name (str): The name of the mission.
        status (str): The status of the mission.
        description (str): The description of the mission.
    """

    __tablename__ = "missions"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    status = Column(String)
    descritption = Column(String)
