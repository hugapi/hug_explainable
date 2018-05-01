"""Defines the toggleable explainable type"""
import hug

from hug_explainable.directive import Explainable


@hug.type(extend=hug.types.smart_boolean)
def explainable_toggle(enabled):
    """If set to True this endpoint will return explainations as well as profiling information."""
    if isinstance(enabled, Explainable):
        return enabled
    
    return Explainable(enabled=enabled)
