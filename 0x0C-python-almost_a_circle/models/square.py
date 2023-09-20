#!/usr/bin/python3
"""Rectangle module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class derived from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self) -> str:
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
