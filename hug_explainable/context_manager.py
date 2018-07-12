"""Provides a simple context manager for adding on to an explanation"""
from datetime import datetime
from contextlib import contextmanager
from copy import deepcopy

from inspect import getframeinfo, stack

import hug


@contextmanager
def explainable(explanation, value=None, explain=None):
    """Mark a section of code as explainable, applying the explanation and time information if requested"""
    if explain is None:
        yield value
        return

    timer = hug.directives.Timer(5)
    caller = getframeinfo(stack()[2][0])
    now = datetime.now()
    given_explanation = {'action': explanation, 'value': deepcopy(value), 'line': caller.lineno,
                         'file': caller.filename, 'time': '{}:{}:{}'.format(now.hour, now.minute, now.second),
                         'datetime': now.isoformat(), 'date': now.date().isoformat()}
    explain.append(given_explanation)
    try:
        yield value
    except Exception as exception:
        exception.explanation = explain
        given_explanation['failed_after'] = float(timer)
        given_explanation['failed_with'] = str(exception.__class__.__name__)
        raise exception

    given_explanation['took'] = float(timer)
