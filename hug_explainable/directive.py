"""A hug directive that enables easy interaction and storage of profiling information and code path explanations."""
from copy import deepcopy
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

    @property
    def enabled(self):
        """Returns True if the explanations are enabled"""
        return bool(self)

    @enabled.setter
    def enabled(self, enable):
        """Switches between enabled and not based on a boolean flag"""
        if enable:
            self.enable()
        else:
            self.disable()

    def insert_into(self, dictionary):
        """Inserts the explanation if there is one, otherwise performs a noop"""
        if self:
            dictionary['explanation'] = self.explanation

    def explained(self, dictionary):
        """Returns an explained version of the dictionary if explainations are enabled,
           otherwise the dictionary unchanged
        """
        self.insert_into(dictionary)
        return dictionary

    def __getitem__(self, index):
        if type(index) == int:
            return self.explanation.__getitem__(index)
        for item in self:
            if item.get(index, None):
                return item

        raise KeyError('Explanation not found')

    def __setitem__(self, explanation, value):
        if type(explanation) == int:
            return self.explanation.__getitem__(explanation)
        if self:
            self.explanation.append({explanation: deepcopy(value), 'took': 0.0})

    def __bool__(self):
        return self.explanation != None

    def __call__(self, explanation, value):
        return explainable(explanation, value, self.explanation)

    def __native_types__(self):
        return self.explanation

    def __iter__(self):
        return self.explanation.__iter__() if self else ().__iter__()

    def __contains__(self, item):
        return self.explanation.__contains__(item) if self else False

    def __len__(self):
        return self.explanation.__len__() if self else 0

    def __delitem__(self, item):
        return self.explanation.__delitem__(item)

    def __reversed__(self):
        return self.explanation.__reversed__() if self else ().__reversed__()

    def append(self, value):
        return self.explanation.append(value)

    def pop(self, index, *kargs, **kwargs):
        return self.explanation.pop(index, *kargs, **kwargs)
