from typing import List, Optional
from pydantic import BaseModel

class Component(BaseModel):
    name: str

class System(BaseModel):
    name: str

class Entity(BaseModel):
    name: str
    components: List[str]
    systems: List[str]

class Scene(BaseModel):
    path: str
    name: str
    description: str
    image: Optional[str]
    entities: List[Entity]
