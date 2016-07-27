import six
import abc


@six.add_metaclass(abc.ABCMeta)
class Term(object):

    @abc.abstractmethod
    def __init__(self): pass

    @abc.abstractmethod
    def _name(self): pass

    @abc.abstractmethod
    def _latex_str(self): pass

    @abc.abstractmethod
    def __add__(self, other): pass
    
    def __radd__(self, other):
        """Reverse addition for creating a list of energy objects."""
        other.add(self)
        return other

    def _repr_latex_(self):
        """A LaTeX representation method in Jupyter notebook."""
        return self._latex_str
