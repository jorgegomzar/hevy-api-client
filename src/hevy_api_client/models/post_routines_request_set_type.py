from enum import Enum


class PostRoutinesRequestSetType(str, Enum):
    DROPSET = "dropset"
    FAILURE = "failure"
    NORMAL = "normal"
    WARMUP = "warmup"

    def __str__(self) -> str:
        return str(self.value)
