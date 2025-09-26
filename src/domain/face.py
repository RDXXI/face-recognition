from dataclasses import dataclass
from typing import List


@dataclass
class Face:
id: str
name: str
embedding: List[float]