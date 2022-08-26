"""A module for testiing githubs automatic test features."""

import numpy

from pandas import DataFrame

class ATest:
    """Test class."""

    def __init__(self) -> None:
        """Initializer of class ATest."""
        self.df = DataFrame()
        self.vec = numpy.ones(0)
