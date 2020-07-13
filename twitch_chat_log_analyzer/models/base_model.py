from abc import ABCMeta
from dataclasses import dataclass
from typing import Dict, Any


@dataclass
class BaseModel(metaclass=ABCMeta):
    data: Dict[str, Any]
