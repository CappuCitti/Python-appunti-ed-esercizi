from dataclasses import dataclass

@dataclass
class Person:
    age: int = 0
    name: str = ""
    surname: str = ""