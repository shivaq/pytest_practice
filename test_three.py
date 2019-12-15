"""Test the Task data type."""

from collections import namedtuple

Task = namedtuple('Task', ['summary', 'owner', 'done', 'id'])

# You can use __new__.__defaults__ to create Task object without specify all the fields
Task.__new__.__defaults__ = (None, None, False, None)


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
