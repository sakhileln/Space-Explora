from pydantic import BaseModel


class MissionBase(BaseModel):
    name: str
    status: str
    descritption: str


class MissionCreate(MissionBase):
    ...


class Mission(MissionBase):
    id: int

    class Config:
        orm_mode = True
