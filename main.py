"""A module for testiing githubs automatic test features."""

import numpy

from pandas import DataFrame

class ATest:
    """Test class."""

    def __init__(self) -> None:
        """Initialize of class ATest."""
        self.dataframe = DataFrame()
        self.vec = numpy.ones(0)

    def print_hello_world(self) -> None:
        """Print 'Hello World!'."""
        print("Hello World!")

    def get_one(self) -> int:
        """Get a one."""
        return 1
