"""Provides a simple context manager for adding on to an explanation"""
from contextlib import contextmanager
from copy import deepcopy

import hug


@contextmanager
def explainable(explanation, value, explain=None):
    """Mark a section of code as explainable, applying the explanation and time information if requested"""
    if explain is None:
        yield value
        return

    timer = hug.directives.Timer(5)
    given_explanation = {explanation: deepcopy(value)}
    explain.append(given_explanation)
    try:
        yield value
    except Exception as exception:
        exception.explanation = explain
        given_explanation['failed_after'] = float(timer)
        given_explanation['failed_with'] = str(exception.__class__.__name__)
        raise exception

    given_explanation['took'] = float(timer)
