"""
   Created by: Sudan Nepali
   Created on: 2024-07-30
"""
from pydantic import BaseModel
from typing import List

class Document(BaseModel):
    text:str = None
    embeddings: List[float] = None
