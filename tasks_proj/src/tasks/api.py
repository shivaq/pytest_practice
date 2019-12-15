"""Main API for tasks project."""

from typing import NamedTuple


class Task(NamedTuple):
    summary: str = None
    owner: str = None
    done: bool = False
    id: int = None
