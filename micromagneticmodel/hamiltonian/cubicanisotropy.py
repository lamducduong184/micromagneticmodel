import joommfutil.typesystem as ts
from .energyterm import EnergyTerm


@ts.typesystem(K1=ts.Real,
               u1=ts.RealVector(size=3),
               u2=ts.RealVector(size=3),
               name=ts.ConstantObjectName)
class CubicAnisotropy(EnergyTerm):
    def __init__(self, K1, u1, u2, name="cubicanisotropy"):
        """Cubic anisotropy energy abstract class.

        Parameters
        ----------
        K1 : Real
            Cubic anisotropy energy constant (J/m**3)
        u1, u2 : (3,) array_like
            Cubic anisotropy axes

        """
        self.K1 = K1
        self.u1 = u1
        self.u2 = u2
        self.name = name

    @property
    def _latex(self):
        a1 = "(\mathbf{m} \cdot \mathbf{u}_{1})^{2}"
        a2 = "(\mathbf{m} \cdot \mathbf{u}_{2})^{2}"
        a3 = "(\mathbf{m} \cdot \mathbf{u}_{3})^{2}"
        return "$-K_{{1}} [{0}{1}+{1}{2}+{2}{0}]$".format(a1, a2, a3)

    @property
    def _repr(self):
        """A representation string property.

        Returns
        -------
        str
            A representation string.

        """
        return ("CubicAnisotropy(K1={}, u1={}, u2={}, "
                "name=\"{}\")").format(self.K1, self.u1, self.u2, self.name)
