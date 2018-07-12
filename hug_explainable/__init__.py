"""Provides an on demand context manager that makes it easy to profile and explain code blocks / paths within hug."""
from hug_explainable._version import current
from hug_explainable.directive import Explainable, explain
from hug_explainable.type import explainable_toggle
from hug_explainable.context_manager import explainable

DONT_EXPLAIN = explainable_toggle(False)

__version__ = current
