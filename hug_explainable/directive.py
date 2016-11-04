"""A hug directive that enables easy interaction and storage of profiling information and code path explanations."""
import hug

from hug_explainable.context_manager import explainable


@hug.directive()
class Explainable(object):
    """Provides a mechanism for explaining and profiling code paths"""
    __slots__ = ('explanation', )

    def __init__(self, enabled=True, **kwargs):
        self.explanation = [] if enabled else None

    def enable(self):
        """Enables storing the recording of explanations of individual code blocks"""
        self.explanation = [] if self.explanation is None else self.explanation

    def disable(self):
        """Disables the recording of explanations of individual code blocks"""
        self.explanation = None

    def insert(self, dictionary):
        """Inserts the explanation if there is one, otherwise performs a noop"""
        if self:
            dictionary['explanation'] = self.explanation

    def __bool__(self):
        return self.explanation != None

    def __call__(self, explanation, value):
        return explainable(explanation, value, self.explanation)

    def __native_types__(self):
        return self.explanation

    def __iter__(self):
        return self.explanation.__iter__()

    def __contains__(self, item):
        return self.explanation.__contains__(item)

    def __len__(self):
        return self.explanation.__len__()

    def __getitem__(self, key):
        return self.explanation.__getitem__(key)

    def __setitem__(self, key, value):
        return self.explanation.__setitem__(key, value)

    def __delitem__(self, item):
        return self.explanation.__delitem__(item)

    def __reversed__(self):
        return self.explanation.__reversed__()

    def __contains__(self, item):
        return self.explanation.__contains__(item)
