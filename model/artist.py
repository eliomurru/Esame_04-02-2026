from dataclasses import dataclass
@dataclass
class Artist:
    id: int
    name: str
    produttivita : int

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return self.__str__()

    def __hash__(self):
        return hash(self.id)