""" Use the Task type to show test failures."""

from tasks import Task


def test_fail_different_task_equality():
    t1 = Task('Sit there', 'brian')
    t2 = Task('do something', 'depalma')

    assert t1 == t2


def test_fail_defferent_dict_equality():
    t1_dict = Task('make sandwich', 'depalma')._asdict()
    t2_dict = Task('make sandwich', 'brian')._asdict()

    assert t1_dict == t2_dict