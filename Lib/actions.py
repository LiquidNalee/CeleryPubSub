from enum import Enum


class Action(Enum):
    CREATION = "CREATION"
    DELETION = "DELETION"
    UPDATE = "UPDATE"
    READ = "READ"

    def __str__(self) -> str:
        return self.value
