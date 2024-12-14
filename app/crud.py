from sqlalchemy.orm import Session
from . import models, schemas


def create_mission(db: Session, mission: schemas.MissionCreate):
    db_mission = models.Mission(**mission.dict())
    db.add(db_mission)
    db.commit()
    db.refresh(db_mission)
    return db_mission


def get_missions(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Mission).offset(skip).limit(limit).all()


def get_mission_by_name(db: Session, name: str):
    return db.query(models.Mission).filter(models.Mission.name == name).first()
