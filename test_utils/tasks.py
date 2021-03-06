"""
Tasks used in tests
"""

from celery_utils import logged_task, persist_on_failure

from .celery import app


@app.task(base=persist_on_failure.LoggedPersistOnFailureTask)
def fallible_task(message=None):
    """
    Simple task to let us test retry functionality.
    """
    if message:
        raise ValueError(message)


@app.task(base=persist_on_failure.LoggedPersistOnFailureTask)
def passing_task():
    """
    This task always passes
    """
    return 5


@app.task(base=logged_task.LoggedTask)
def simple_logged_task(a, b, c):  # pylint: disable=invalid-name
    """
    This task gets logged
    """
    return a + b + c


@app.task(base=logged_task.LoggedTask)
def failed_logged_task():
    """
    Simple task to let us test logging on failure.
    """
    raise ValueError()
