#!/usr/bin/python3
"""Task: 12.My integer"""


class MyInt(int):
    """class overrides some operators from int class"""

    def __eq__(self, __value: object) -> bool:
        return not super().__eq__(__value)

    def __ne__(self, __value: object) -> bool:
        return not super().__ne__(__value)
