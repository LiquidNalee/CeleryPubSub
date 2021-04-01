from enum import Enum


class BindingKey(Enum):
    ESTIMA = "ESTIMA"
    LEAD = "LEAD"

    def __str__(self) -> str:
        return self.value
