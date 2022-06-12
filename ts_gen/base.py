import numpy as np
from typing import Tuple, Protocol


class TsGenrator(Protocol):
    def generate(self) -> Tuple[np.ndarray, np.ndarray]:
        """Generate x and y of a timeseries, both are numpy arrays"""
        ...