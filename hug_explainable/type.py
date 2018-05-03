"""Defines the toggleable explainable type"""
import hug

from hug_explainable.directive import Explainable


class ExplainableToggle(hug.types.SmartBoolean):
    """If set to True this endpoint will return explainations as well as profiling information."""

    def __call__(self, enabled):
        if isinstance(enabled, Explainable):
            return enabled
        return Explainable(enabled=super().__call__(enabled))


explainable_toggle = ExplainableToggle()
