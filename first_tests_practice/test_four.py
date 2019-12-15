""" Test the Task data type."""

# from collections import namedtuple
# Task = namedtuple('Task', ['summary', 'owner', 'done', 'id'])
# Task.__new__.__defaults__ = (None, None, False, None)
import pytest
from typing import NamedTuple


class Task(NamedTuple):
    summary: str = None
    owner: str = None
    done: bool = False
    id: int = None


@pytest.mark.run_these_please
def test_asdict():
    """_asdict() sould return a dictionary """

    # Instantiate Task
    t_task = Task('do something', 'okken', True, 21)
    # Convert to dictionary
    t_dict = t_task._asdict()
    expected = {'summary': 'do something', 'owner': 'okken', 'done': True, 'id': 21}
    assert t_dict == expected


@pytest.mark.run_these_please
def test_replace():
    """ replace() should change passed in fields"""

    t_before = Task('finish book', 'brian', False)
    # returns a new namedtuple
    t_after = t_before._replace(id=10, done=True)
    t_expected = Task('finish book', 'brian', True, 10)
    assert t_after == t_expected
