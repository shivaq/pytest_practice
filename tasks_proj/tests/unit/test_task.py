""" Test the Task data type."""

# from collections import namedtuple
# Task = namedtuple('Task', ['summary', 'owner', 'done', 'id'])
# Task.__new__.__defaults__ = (None, None, False, None)
from tasks import Task


def test_asdict():
    """_asdict() sould return a dictionary """

    # Instantiate Task
    t_task = Task('do something', 'okken', True, 21)
    # Convert to dictionary
    t_dict = t_task._asdict()
    expected = {'summary': 'do something', 'owner': 'okken', 'done': True, 'id': 21}
    assert t_dict == expected


def test_replace():
    """ replace() should change passed in fields"""

    t_before = Task('finish book', 'brian', False)
    # returns a new namedtuple
    t_after = t_before._replace(id=10, done=True)
    t_expected = Task('finish book', 'brian', True, 10)
    assert t_after == t_expected


def test_defaults():
    """Using no parameters should involve defaults"""
    t1 = Task()
    t2 = Task(None, None, False, None)

    assert t1 == t2


def test_member_access():
    """Check .field functionality of namedtuple."""

    t = Task('buy milk', 'brian')

    assert t.summary == 'buy milk'
    assert t.owner == 'brian'
    assert (t.done, t.id) == (False, None)
