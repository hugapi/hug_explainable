"""Provides an on demand context manager that makes it easy to profile and explain code blocks / paths within hug."""
from hug_explainable._version import current
from hug_explainable.directive import Explainable
from hug_explainable.context_manager import explainable

__version__ = current
