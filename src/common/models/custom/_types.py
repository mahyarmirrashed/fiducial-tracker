"""Define appropriately the NumPy ndarray to use."""

from numpy.lib import NumpyVersion
from typing import Any, TypeVar

import numpy as np
import sys

T = TypeVar("T", bound=np.generic)

if sys.version_info < (3, 9) or NumpyVersion(np.__version__) < "1.22.0":
  ndarray = np.ndarray
else:
  ndarray = np.ndarray[Any, T]
