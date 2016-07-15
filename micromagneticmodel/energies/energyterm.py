import abc
from hamiltonian import Hamiltonian


class EnergyTerm(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def __init__(self): pass

    @abc.abstractmethod
    def calculator_script(self): pass

    @abc.abstractmethod
    def _name(self): pass

    @abc.abstractmethod
    def _latex_str(self): pass

    def __add__(self, other):
        """Addition for creating a list of energy objects."""
        hamiltonian = Hamiltonian()
        hamiltonian.add(self)
        hamiltonian.add(other)
        return hamiltonian

    def __radd__(self, other):
        """Reverse addition for creating a list of energy objects."""
        other.add(self)
        return other

    def _repr_latex_(self):
        """A LaTeX representation method."""
        return self._latex_str