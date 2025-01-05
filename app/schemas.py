"""
Module for defining Pydantic models for Mission data validation.

This module includes Pydantic models used for validating and serializing
mission data. The models are designed to be used in the context of
FastAPI or other Python web frameworks that integrate with Pydantic for
data validation.

Models:
    - MissionBase: Base class for mission data validation (name, status, description).
    - MissionCreate: Model used when creating a new mission.
    - Mission: Model that includes the mission ID, used for returning mission data.
"""

from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class MissionBase(BaseModel):
    """
    Base model for mission data validation.

    This model defines the common fields for a mission, including the name,
    status, and description. It serves as the foundation for other mission-related
    models.

    Attributes:
        name (str): The name of the mission.
        status (str): The status of the mission.
        description (str): The description of the mission.
    """

    name: str
    status: str
    description: Optional[str] = "No description available."
    launch_date: Optional[datetime] = None


class MissionCreate(MissionBase):
    """
    Model used for creating a new mission.

    This model inherits from `MissionBase` and is used specifically for creating
    new missions, and may not include an ID since it is only required when
    retrieving or updating existing records.
    """


class Mission(MissionBase):
    """
    Model for representing a mission with an ID.

    This model includes all the fields from `MissionBase` along with the
    mission's unique identifier (ID). It is used when returning mission
    data that includes the mission's ID.

    Attributes:
        id (int): The unique identifier of the mission.

    Config:
        orm_mode (bool): Tells Pydantic to treat ORM models as dictionaries.
    """

    id: int

    # pylint: disable=too-few-public-methods
    class Config:
        """Tell Pydantic to treat ORM models as dictionaries."""

        # orm_mode = True
        from_attributes = True
